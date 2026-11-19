"""Time every word of the exact script against the speech in the video.

Usage: python3 timing.py input.mp4 "the exact spoken line, word for word" words.json
Finds the voiced parts of the audio and spreads the words over them by length.
Join words that belong together with "_" (for example: الـ_captions) so they stay one caption word.
Prints a numbered list of the words with their times, so the plan can point at word numbers.
"""
import sys, json, subprocess, tempfile, os
import numpy as np, soundfile as sf

SR = 48000


def audio(path):
    tmp = os.path.join(tempfile.mkdtemp(), 'a.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-vn', '-ac', '1', '-ar', str(SR), tmp], check=True)
    a, _ = sf.read(tmp)
    return a


def voiced(a, merge=0.14, thr_db=24):
    hop = int(0.01 * SR)
    e = np.array([np.sqrt(np.mean(a[i:i + hop] ** 2)) for i in range(0, len(a) - hop, hop)])
    db = 20 * np.log10(e + 1e-9)
    v = db > np.percentile(db, 97) - thr_db
    segs = []; i = 0
    while i < len(v):
        if v[i]:
            j = i
            while j < len(v) and v[j]:
                j += 1
            segs.append([i * 0.01, j * 0.01]); i = j
        else:
            i += 1
    out = []
    for s in segs:
        if out and s[0] - out[-1][1] < merge:
            out[-1][1] = s[1]
        else:
            out.append(s)
    return [s for s in out if s[1] - s[0] > 0.06]


def word_times(words, segs):
    L = [max(2, len(w.replace('_', '').replace('؟', '').replace('،', '').replace('?', '').replace(',', ''))) for w in words]
    tv = sum(b - a for a, b in segs); tl = sum(L)

    def at(fr):
        x = fr * tv
        for a, b in segs:
            if x <= b - a + 1e-9:
                return a + x
            x -= b - a
        return segs[-1][1]
    out = []; c = 0
    for w, l in zip(words, L):
        out.append([w, round(at(c / tl), 3), round(at((c + l) / tl), 3)]); c += l
    return out


if __name__ == '__main__':
    src, line, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    wt = word_times(line.split(), voiced(audio(src)))
    json.dump(wt, open(dst, 'w'), ensure_ascii=False, indent=0)
    for i, (w, a, b) in enumerate(wt):
        print(f'{i:2d}  {a:6.2f}-{b:6.2f}  {w}')
