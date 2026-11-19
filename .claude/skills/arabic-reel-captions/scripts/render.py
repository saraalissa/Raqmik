"""Render the caption plan onto a talking video (keeps the original sound).

  python3 render.py --video in.mp4 --matte matte.mp4 --plan plan.json --out out.mp4
  python3 render.py ... --preview 0.8,2.3,3.6      # writes preview_<t>.jpg instead of a video

plan.json = {"grade": true, "face": [x, y] (optional spotlight centre), "events": [ ... ]}
Each event has a "style" and times in seconds (word times come from timing.py). See SKILL.md.
"""
import sys, os, json, argparse, subprocess
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import capfx2 as C


def draw(ev, F, M, t, tops):
    st = ev['style']; occ = M if ev.get('behind') else None
    if st == 'line':
        C.style_line(F, t, ev['words'], ev['t1'], ev.get('x', 540), ev.get('y', 1250), ev.get('size', 92), occl=occ)
    elif st == 'hero':
        C.style_hero(F, t, ev['text'], ev['t0'], ev['t1'], ev.get('x', 540), ev.get('y', 1420), ev.get('size', 270),
                     ev.get('fill', 'creamgrad'), tuple(ev.get('glow', (255, 170, 60))), occl=occ, font_name=ev.get('font', 'callig'))
    elif st == 'arc':
        cx, cy = ev.get('cx', 540), ev.get('cy', 600)
        C.style_arc(F, t, ev['words'], ev['t1'], cx, cy, ev.get('rx', 450), ev.get('ry', 480), ev.get('which', 'top'), ev.get('size', 110),
                    ev.get('fill', 'white'), tuple(ev.get('glow', (255, 180, 74))), ev.get('off0', 0), ev.get('off1', 0),
                    occl=M if ev.get('which', 'top') == 'top' else None)
    elif st == 'neon':
        C.style_neon(F, t, ev['text'], ev['t0'], ev['t1'], ev.get('x', 540), ev.get('y', 200), ev.get('size', 230), tuple(ev.get('colour', (255, 70, 200))), occl=M)
    elif st == 'glass':
        C.style_glass(F, t, ev['text'], ev['t0'], ev['t1'], ev.get('x', 540), ev.get('y', 220), ev.get('size', 320), occl=M)
    elif st == 'wall':
        C.style_wall(F, t, ev['lines'], ev['t1'], ev.get('x', 880), ev.get('y', 350), ev.get('size', 84), ev.get('fill', 'ink'), ev.get('tilt', -32), occl=M)
    elif st == 'chips':
        C.style_chips(F, t, ev['items'], ev['t1'])
    elif st == 'counter':
        C.style_counter(F, t, ev['t0'], ev['t1'], ev.get('x', 540), ev.get('y', 140), ev.get('start', 1), ev.get('end', 1305), ev.get('label', 'frame'))
    else:
        raise SystemExit('unknown style ' + st)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--video', required=True); ap.add_argument('--matte', required=True); ap.add_argument('--plan', required=True)
    ap.add_argument('--out', default='captioned.mp4'); ap.add_argument('--preview', default='')
    a = ap.parse_args(); plan = json.load(open(a.plan))
    cv = cv2.VideoCapture(a.video); cm = cv2.VideoCapture(a.matte); fps = cv.get(cv2.CAP_PROP_FPS) or 30
    W = int(cv.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cv.get(cv2.CAP_PROP_FRAME_HEIGHT))
    face = tuple(plan['face']) if plan.get('face') else None
    want = [float(x) for x in a.preview.split(',') if x]; p = None
    if not want:
        p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(fps), '-i', '-',
                              '-i', a.video, '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                              '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', a.out], stdin=subprocess.PIPE)
    i = 0
    while True:
        ok, f = cv.read(); ok2, m = cm.read()
        if not ok or not ok2: break
        t = i / fps
        if want and not any(abs(t - w) < 0.5 / fps for w in want): i += 1; continue
        M = m[..., 0].astype(np.float32) / 255
        F = C.grade(f, face) if plan.get('grade', True) else f.astype(np.float32) / 255
        for ev in plan['events']: draw(ev, F, M, t, None)
        out = (np.clip(F, 0, 1) * 255).astype(np.uint8)
        if p: p.stdin.write(out.tobytes())
        else: cv2.imwrite(f'preview_{t:.2f}.jpg', out)
        i += 1
    if p: p.stdin.close(); p.wait()
    print('done', i, 'frames')


if __name__ == '__main__':
    main()
