"""Premium Arabic kinetic captions for vertical talking videos (no browser needed).

Looks: modern sans (Alexandria) for small words, gold/cream calligraphy (Aref Ruqaa) for the key word,
elegant italic (Amiri Bold Italic) for English words. Every word blurs in, rises and settles; key words pop.
Styles: line, hero, arc (text bent around the head), behind (big word behind the head), neon, glass,
wall (text painted on the wall in perspective), box (word on a coloured box), chips (UI pills), counter.
Plus grade(): warm cinematic look with a soft spotlight on the face (no cut-out, so no halo).
"""
import os, math
from functools import lru_cache
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter, features

FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fonts') + os.sep
FONTS = {'sans': ('Alexandria[wght].ttf', 700), 'sans_xb': ('Alexandria[wght].ttf', 800), 'sans_md': ('Alexandria[wght].ttf', 600),
         'sans_lt': ('Alexandria[wght].ttf', 300), 'callig': ('ArefRuqaa-Bold.ttf', None), 'latin_it': ('Amiri-BoldItalic.ttf', None),
         'neon': ('ReemKufi[wght].ttf', 500)}
try:
    RAQM = bool(features.check('raqm'))
except Exception:
    RAQM = False
COL = {'white': (255, 255, 255), 'cream': (255, 244, 214), 'gold': (255, 211, 107), 'red': (229, 50, 45), 'blue': (47, 124, 246),
       'yellow': (255, 210, 63), 'ink': (61, 33, 22), 'pink': (255, 70, 200)}

def isar(s): return any('؀' <= c <= 'ۿ' for c in s)

@lru_cache(maxsize=64)
def font(name, size):
    fn, w = FONTS[name]
    f = ImageFont.truetype(FD + fn, int(size), layout_engine=ImageFont.Layout.RAQM if RAQM else ImageFont.Layout.BASIC)
    if w:
        try:
            axes = f.get_variation_axes(); f.set_variation_by_axes([w] + [a.get('default', 0) for a in axes[1:]])
        except Exception:
            pass
    return f

def _kw(t):
    if not isar(t): return {}
    if not RAQM: raise RuntimeError('Arabic letters need Pillow with raqm: apt-get install -y libraqm0 libfribidi0 (or pip install -U pillow)')
    return dict(direction='rtl', language='ar')

@lru_cache(maxsize=512)
def mask(text, fname, size):
    f = font(fname, size); bb = f.getbbox(text, **_kw(text)); pad = int(size * 0.5)
    im = Image.new('L', (bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad), 0)
    ImageDraw.Draw(im).text((pad - bb[0], pad - bb[1]), text, font=f, fill=255, **_kw(text))
    return np.asarray(im, np.float32) / 255

def colour_fill(A, fill):
    """fill: colour name / rgb, or 'goldgrad' / 'creamgrad' vertical gradients."""
    h, w = A.shape
    if fill in ('goldgrad', 'creamgrad'):
        top, mid, bot = ((255, 246, 214), (255, 215, 106), (240, 164, 58)) if fill == 'goldgrad' else ((255, 255, 255), (255, 243, 214), (255, 217, 140))
        rows = np.array([np.array(top) * (1 - min(1, v / 0.5)) + np.array(mid) * min(1, v / 0.5) if v < 0.5 else np.array(mid) * (1 - (v - 0.5) / 0.5) + np.array(bot) * ((v - 0.5) / 0.5) for v in np.linspace(0, 1, h)])
        return np.repeat(rows[:, None, :], w, 1).astype(np.float32)
    rgb = COL.get(fill, fill) if isinstance(fill, str) else fill
    return np.ones((h, w, 3), np.float32) * np.array(rgb, np.float32)

def sprite(text, fname='sans', size=70, fill='white', glow=None, glow_r=0.12, shadow=0.55):
    """RGBA float sprite (h,w,4) with optional glow colour and soft drop shadow."""
    A = mask(text, fname, size); h, w = A.shape
    rgb = colour_fill(A, fill); out = np.zeros((h, w, 4), np.float32)
    if shadow:
        sa = cv2.GaussianBlur(np.roll(A, int(size * 0.06), 0), (0, 0), size * 0.09) * shadow
        out[..., 3] = sa
    if glow:
        ga = cv2.GaussianBlur(A, (0, 0), size * glow_r) * 1.4
        gc = np.array(COL.get(glow, glow) if isinstance(glow, str) else glow, np.float32)
        a = np.clip(ga, 0, 1); out[..., :3] = out[..., :3] * (1 - a[..., None]) + gc * a[..., None]; out[..., 3] = np.maximum(out[..., 3], a * 0.8)
    out[..., :3] = out[..., :3] * (1 - A[..., None]) + rgb * A[..., None]
    out[..., 3] = np.maximum(out[..., 3], A)
    return out

def trim(s, margin):
    a = s[..., 3] > 0.03; ys, xs = np.where(a)
    if len(xs) == 0: return s
    x0, x1 = max(0, xs.min() - margin), min(s.shape[1], xs.max() + 1 + margin); y0, y1 = max(0, ys.min() - margin), min(s.shape[0], ys.max() + 1 + margin)
    return s[y0:y1, x0:x1]

def blit(frame, spr, cx, cy, alpha=1.0, scale=1.0, blur=0.0, rot=0.0, occl=None):
    """Alpha-composite sprite centred at (cx,cy) onto float BGR frame (0..1). occl = speaker matte (she covers it)."""
    s = spr
    if scale != 1.0: s = cv2.resize(s, (max(2, int(s.shape[1] * scale)), max(2, int(s.shape[0] * scale))), interpolation=cv2.INTER_LINEAR)
    if rot:
        h, w = s.shape[:2]; M = cv2.getRotationMatrix2D((w / 2, h / 2), rot, 1.0); s = cv2.warpAffine(s, M, (w, h))
    if blur > 0.3: s = cv2.GaussianBlur(s, (0, 0), blur)
    H, W = frame.shape[:2]; h, w = s.shape[:2]; x0 = int(round(cx - w / 2)); y0 = int(round(cy - h / 2))
    xa, ya, xb, yb = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    if xb <= xa or yb <= ya: return
    sub = s[ya - y0:yb - y0, xa - x0:xb - x0]; a = np.clip(sub[..., 3:4] * alpha, 0, 1)
    if occl is not None: a = a * (1 - occl[ya:yb, xa:xb, None])
    frame[ya:yb, xa:xb] = frame[ya:yb, xa:xb] * (1 - a) + (sub[..., 2::-1] / 255) * a

def ease_out(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 3
def ease_back(x, s=1.6): x = min(max(x, 0), 1); return 1 + (s + 1) * (x - 1) ** 3 + s * (x - 1) ** 2

def state(t, t0, t1, pop=False, in_d=0.3, out_d=0.22):
    """(alpha, blur, dy, scale) for a word that appears at t0 and leaves at t1."""
    p = ease_out((t - t0) / in_d)
    a, b, dy, sc = p, (1 - p) * 14, (1 - p) * 22, 0.9 + 0.1 * p
    if pop: sc = 0.55 + 0.45 * ease_back((t - t0) / 0.4)
    dy -= max(0, t - t0) * 8; sc *= 1 + max(0, t - t0) * 0.02
    q = min(1, max(0, (t1 - t) / out_d)); a *= q; b += (1 - q) * 12; dy -= (1 - q) * 14
    return a, b, dy, sc

# ---------------- styles (all draw on a float BGR frame 0..1) ----------------
def style_line(frame, t, words, t1, x, y, size=92, gap=0.12, occl=None):
    """words: list of dicts {w, t, font?, fill?, glow?, size?, box?}. Laid out right-to-left, centred at (x,y)."""
    if t < words[0]['t'] - 0.01 or t >= t1: return
    sprs = []
    for d in words:
        s = sprite(d['w'], d.get('font', 'sans'), d.get('size', size), d.get('fill', 'white'), d.get('glow'), shadow=0.55)
        A0 = (mask(d['w'], d.get('font', 'sans'), d.get('size', size)) > 0.03); xs = np.where(A0.any(0))[0]; ys = np.where(A0.any(1))[0]
        s = s[:, max(0, xs.min() - int(size * 0.12)):xs.max() + int(size * 0.12)]
        if d.get('box'):
            h, w = s.shape[:2]; bx = np.zeros((h, w + int(size * 0.4), 4), np.float32)
            im = Image.new('RGBA', (bx.shape[1], h), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle((0, int(h * 0.18), bx.shape[1] - 1, int(h * 0.86)), radius=int(size * 0.2), fill=tuple(COL.get(d['box'], d['box'])) + (255,))
            bx = np.asarray(im, np.float32).copy(); bx[..., 3] /= 255
            ox = (bx.shape[1] - w) // 2; reg = bx[:, ox:ox + w]; a = s[..., 3:4]
            reg[..., :3] = reg[..., :3] * (1 - a) + s[..., :3] * a; reg[..., 3] = np.maximum(reg[..., 3], s[..., 3]); s = bx
        sprs.append(s)
    widths = [s.shape[1] for s in sprs]; total = sum(widths) + gap * size * (len(sprs) - 1)
    cur = x + total / 2                               # right edge (RTL)
    rtl = any(isar(d['w']) for d in words)
    order = list(range(len(sprs)))
    if not rtl: cur = x - total / 2
    for i in order:
        wd = widths[i]; cx = cur - wd / 2 if rtl else cur + wd / 2
        a, b, dy, sc = state(t, words[i]['t'], t1, words[i].get('pop', False))
        if a > 0.01: blit(frame, sprs[i], cx, y + dy, a, sc, b, occl=occl)
        cur = cur - wd - gap * size if rtl else cur + wd + gap * size

def style_hero(frame, t, text, t0, t1, x, y, size=270, fill='creamgrad', glow=(255, 170, 60), occl=None, font_name='callig'):
    """One big key word in calligraphy that pops in with a glow."""
    if not (t0 - 0.01 <= t < t1): return
    s = sprite(text, font_name, size, fill, glow, 0.1, shadow=0.7)
    a, b, dy, sc = state(t, t0, t1, pop=True)
    blit(frame, s, x, y + dy, a, sc, b, occl=occl)

def style_arc(frame, t, words, t1, cx, cy, rx, ry, which='top', size=110, fill='white', glow=(255, 180, 74), off0=0.0, off1=0.0, occl=None):
    """Phrase bent along the top (behind the head when occl is given) or bottom (in front) of an ellipse around the head.
    off0/off1: slide along the arc in px over the event (orbit feel)."""
    if t < words[0]['t'] - 0.01 or t >= t1: return
    f = font('sans_xb', size); kw = _kw(' '.join(d['w'] for d in words))
    txt = ' '.join(d['w'] for d in words); bb = f.getbbox(txt, **kw); pad = int(size * 0.6)
    W_, H_ = bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad
    # per-word alpha: draw each prefix and diff (keeps Arabic joining intact)
    A = np.zeros((H_, W_), np.float32); prev = np.zeros_like(A)
    for i, d in enumerate(words):
        im = Image.new('L', (W_, H_), 0); pre = ' '.join(x['w'] for x in words[:i + 1])
        # draw prefix right-aligned for RTL so earlier words keep their place
        pb = f.getbbox(pre, **kw); px = (W_ - pad) - (pb[2] - pb[0]) - pb[0] if kw else pad - bb[0]
        ImageDraw.Draw(im).text((px, pad - bb[1]), pre, font=f, fill=255, **kw)
        cur = np.asarray(im, np.float32) / 255; part = np.clip(cur - prev, 0, 1); prev = np.maximum(prev, cur)
        a, _, _, _ = state(t, d['t'], t1); A += part * a
    A = np.clip(A, 0, 1); h, w = A.shape
    glowA = cv2.GaussianBlur(A, (0, 0), size * 0.12) * 1.3
    H, W = frame.shape[:2]
    prog = min(1, max(0, (t - words[0]['t']) / max(0.1, t1 - words[0]['t']))); off = off0 + (off1 - off0) * prog
    ang = np.linspace(-np.pi, 0, 3000) if which == 'top' else np.linspace(np.pi, 0, 3000)
    xs = cx + rx * np.cos(ang); ys = cy + ry * np.sin(ang)
    cum = np.concatenate([[0], np.cumsum(np.hypot(np.diff(xs), np.diff(ys)))]); mid = cum[-1] / 2
    y0, y1 = (max(0, int(cy - ry - size * 1.6)), min(H, int(cy + size * 0.2))) if which == 'top' else (max(0, int(cy - size * 0.2)), min(H, int(cy + ry + size * 1.6)))
    yy, xx = np.mgrid[y0:y1, 0:W].astype(np.float32)
    th = np.arctan2((yy - cy) / ry, (xx - cx) / rx); r = np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)
    loc = np.sqrt((rx * np.cos(th)) ** 2 + (ry * np.sin(th)) ** 2)
    if which == 'top':
        s = np.interp(th, ang, cum) - mid; d = (r - 1) * loc; valid = th <= 0
        u = s + w / 2 - off; v = (h - pad * 0.9) - d
    else:
        s = np.interp(th, ang[::-1], cum[::-1]) - mid; d = (1 - r) * loc; valid = th >= 0
        u = (w / 2) - s - off; v = (h - pad * 0.9) - d
        u = w - u  # keep reading order right-to-left along the smile
    mx, my = u.astype(np.float32), v.astype(np.float32)
    Aw = cv2.remap(A, mx, my, cv2.INTER_LINEAR, borderValue=0) * valid; Gw = cv2.remap(glowA, mx, my, cv2.INTER_LINEAR, borderValue=0) * valid
    col = np.array(COL.get(fill, fill) if isinstance(fill, str) else fill, np.float32)[::-1] / 255; gcol = np.array(glow, np.float32)[::-1] / 255
    reg = frame[y0:y1]; occ = (1 - occl[y0:y1]) if occl is not None else 1.0
    ga = np.clip(Gw * 0.7, 0, 1)[..., None] * (occ[..., None] if occl is not None else 1)
    reg[:] = reg * (1 - ga) + gcol * ga
    aa = np.clip(Aw, 0, 1)[..., None] * (occ[..., None] if occl is not None else 1)
    reg[:] = reg * (1 - aa) + col * aa

def style_neon(frame, t, text, t0, t1, x, y, size=230, colour=(255, 70, 200), occl=None):
    """Neon tube sign that flickers on; behind the speaker when occl is given."""
    if not (t0 <= t < t1): return
    d = t - t0; on = 0.12 if (d < 0.04 or 0.08 < d < 0.12 or 0.19 < d < 0.24) else 1.0
    on *= min(1, (t1 - t) / 0.2)
    A = mask(text, 'neon', size); tube = cv2.dilate(A, np.ones((3, 3), np.uint8))
    c = np.array(colour, np.float32)[::-1] / 255
    L = sum(cv2.GaussianBlur(tube, (0, 0), size * k)[..., None] * g for k, g in ((0.03, 1.4), (0.1, 1.2), (0.28, 0.9))) * c + tube[..., None] * (0.35 * c + 0.75)
    L = np.clip(L, 0, 1.6) * on; h, w = A.shape; x0, y0 = int(x - w / 2), int(y - h / 2); H, W = frame.shape[:2]
    xa, ya, xb, yb = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    Ls = L[ya - y0:yb - y0, xa - x0:xb - x0]
    if occl is not None: Ls = Ls * (1 - occl[ya:yb, xa:xb, None])
    reg = frame[ya:yb, xa:xb]; reg[:] = 1 - (1 - reg) * (1 - np.clip(Ls, 0, 1)) + np.clip(Ls - 1, 0, 1) * 0.4

def style_glass(frame, t, text, t0, t1, x, y, size=320, occl=None):
    """Liquid-glass letters: the room is refracted and frosted through them."""
    if not (t0 <= t < t1): return
    a_, b_, dy, sc = state(t, t0, t1, pop=True)
    A = mask(text, 'sans_xb', int(size * sc)); h, w = A.shape; H, W = frame.shape[:2]
    x0, y0 = int(x - w / 2), int(y + dy - h / 2); xa, ya, xb, yb = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    m = A[ya - y0:yb - y0, xa - x0:xb - x0] * a_; sz = float(size)
    soft = cv2.GaussianBlur(m, (0, 0), sz * 0.05)
    gx = cv2.Sobel(soft, cv2.CV_32F, 1, 0, ksize=5); gy = cv2.Sobel(soft, cv2.CV_32F, 0, 1, ksize=5); k = float(sz * 0.45)
    gyy, gxx = np.mgrid[ya:yb, xa:xb].astype(np.float32)
    ref = cv2.remap(frame.astype(np.float32), (gxx - gx * k).astype(np.float32), (gyy - gy * k).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    ref = cv2.GaussianBlur(ref, (0, 0), 3.0) * 0.95 + np.array([0.10, 0.07, 0.04], np.float32)
    light = np.clip(-(gx + gy) * 5, 0, 1)[..., None]; rim = np.clip(cv2.morphologyEx(m, cv2.MORPH_GRADIENT, np.ones((3, 3), np.uint8)), 0, 1)[..., None]
    g = ref + light * 1.1 + rim * 0.75
    occ = (1 - occl[ya:yb, xa:xb])[..., None] if occl is not None else 1.0
    al = m[..., None] * occ; sh = cv2.GaussianBlur(m, (0, 0), 12)[..., None] * 0.35 * occ
    reg = frame[ya:yb, xa:xb]; reg[:] = (reg * (1 - sh)) * (1 - al) + np.clip(g, 0, 1.2) * al

def style_wall(frame, t, lines, t1, x, y, size=84, fill='ink', tilt=-32, occl=None):
    """Lines painted on the wall in perspective (behind the speaker). lines: list of dicts {w, t, font?, fill?}."""
    if t < lines[0]['t'] - 0.01 or t >= t1: return
    for i, d in enumerate(lines):
        a, b, _, _ = state(t, d['t'], t1)
        if a <= 0.01: continue
        s = sprite(d['w'], d.get('font', 'sans_xb'), d.get('size', size), d.get('fill', fill), None, shadow=0)
        h, w = s.shape[:2]; k = math.tan(math.radians(abs(tilt))) * 0.35
        src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
        dst = np.float32([[0, h * k], [w, 0], [w, h], [0, h * (1 - k)]]) if tilt < 0 else np.float32([[0, 0], [w, h * k], [w, h * (1 - k)], [0, h]])
        M = cv2.getPerspectiveTransform(src, dst); s2 = cv2.warpPerspective(s, M, (w, h))
        blit(frame, s2, x, y + i * size * 1.15, a * 0.92, 1.0, b, occl=occl)

def chip(text, bg='white', fg='ink', size=48, outline=None):
    """UI pill sprite."""
    f = font('sans', size); kw = _kw(text); bb = f.getbbox(text, **kw); padx = int(size * 0.7); h = int(size * 1.9)
    w = bb[2] - bb[0] + 2 * padx; im = Image.new('RGBA', (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    bgc = COL.get(bg, bg) if isinstance(bg, str) else bg; fgc = COL.get(fg, fg) if isinstance(fg, str) else fg
    d.rounded_rectangle((20, 20, 20 + w, 20 + h), radius=h // 2, fill=tuple(bgc) + (240,), outline=outline, width=3 if outline else 0)
    d.text((20 + padx - bb[0], 20 + (h - (bb[3] - bb[1])) / 2 - bb[1]), text, font=f, fill=tuple(fgc) + (255,), **kw)
    a = np.asarray(im, np.float32).copy(); a[..., 3] /= 255
    sh = cv2.GaussianBlur(a[..., 3], (0, 0), 10) * 0.45; a[..., 3] = np.maximum(a[..., 3], sh); return a

def style_chips(frame, t, items, t1, occl=None):
    """items: list of {text, x, y, t, bg?, fg?, rot?}: UI pills that pop in one after another."""
    for it in items:
        if not (it['t'] <= t < t1): continue
        s = chip(it['text'], it.get('bg', 'white'), it.get('fg', 'ink'), it.get('size', 60))
        a, b, dy, sc = state(t, it['t'], t1, pop=True)
        blit(frame, s, it['x'], it['y'] + dy, a, sc, b, it.get('rot', 0))

def style_counter(frame, t, t0, t1, x, y, start=1, end=1305, label='frame'):
    """Editor-style frame counter pill."""
    if not (t0 <= t < t1): return
    p = (t - t0) / (t1 - t0); n = int(start + p * (end - start))
    s = chip(f'{label} {n:04d} / {end}', (15, 20, 35), (156, 195, 255), 34)
    a, b, dy, sc = state(t, t0, t1); blit(frame, s, x, y, a, 1.0, b)

# ---------------- cinematic grade ----------------
_cache = {}
def grade(frame, face_c=None, exp=0.92, warm=0.7, vig=0.62, sat=0.9, leak=0.55, bloom=0.2, grain=2.2):
    """Warm cinematic look on the whole frame with a soft spotlight on the face. frame: BGR uint8 -> float 0..1."""
    H, W = frame.shape[:2]; key = (H, W, face_c, vig, leak)
    if key not in _cache:
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); fcx, fcy = face_c or (W / 2, H * 0.32)
        r = np.sqrt(((xx - fcx) / (W * 0.72)) ** 2 + ((yy - fcy) / (H * 0.52)) ** 2)
        V = (1 - vig * np.clip(r, 0, 1.6) ** 1.7)[..., None]
        rad = lambda cx, cy, rx, ry: np.clip(1 - (((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2), 0, 1) ** 2
        L = rad(W * 0.02, H * 0.18, W * 0.75, H * 0.32)[..., None] * np.array([0.10, 0.36, 0.78], np.float32) * leak \
            + rad(W, H * 0.30, W * 0.55, H * 0.25)[..., None] * np.array([0.08, 0.25, 0.55], np.float32) * leak * 0.6
        _cache[key] = (V, L)
    V, L = _cache[key]
    x = frame.astype(np.float32) / 255 * exp * (np.array([0.88, 0.96, 1.05], np.float32) ** warm)
    x = np.clip(x, 0, 1); x = x + 0.55 * (x - x ** 2) * (2 * x - 1)
    lum = x.mean(-1, keepdims=True); x = lum + (x - lum) * sat
    x = 1 - (1 - np.clip(x * V, 0, 1)) * (1 - L)
    hi = np.clip(x - 0.70, 0, 1); x = x + cv2.GaussianBlur(hi, (0, 0), 24) * bloom * 2.2
    x = x + np.random.randn(H, W, 1).astype(np.float32) * (grain / 255)
    return np.clip(x, 0, 1)
