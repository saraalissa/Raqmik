"""Cut the speaker out of every frame (alpha matte) with Robust Video Matting.

Usage: python3 matte.py input.mp4 matte.mp4
Writes a grey video the same size as the input: white = speaker, black = background.
The model (about 15 MB) is downloaded once from the official GitHub release.
"""
import os, sys, subprocess, urllib.request
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, '..', 'models', 'rvm_mobilenetv3_fp32.onnx')
URL = 'https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx'


def ensure_model():
    if os.path.exists(MODEL) and os.path.getsize(MODEL) > 1_000_000:
        return MODEL
    os.makedirs(os.path.dirname(MODEL), exist_ok=True)
    print('downloading matting model ...', flush=True)
    urllib.request.urlretrieve(URL, MODEL)
    return MODEL


def run(src, out, ratio=0.25):
    import onnxruntime as ort
    sess = ort.InferenceSession(ensure_model(), providers=['CPUExecutionProvider'])
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    rec = [np.zeros([1, 1, 1, 1], np.float32)] * 4
    dr = np.array([ratio], np.float32)
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'gray', '-s', f'{W}x{H}',
                          '-r', str(fps), '-i', '-', '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out],
                         stdin=subprocess.PIPE)
    n = 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        x = cv2.cvtColor(f, cv2.COLOR_BGR2RGB).astype(np.float32).transpose(2, 0, 1)[None] / 255
        fgr, pha, *rec = sess.run(None, {'src': x, 'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3],
                                         'downsample_ratio': dr})
        p.stdin.write((pha[0, 0] * 255).clip(0, 255).astype(np.uint8).tobytes())
        n += 1
        if n % 60 == 0:
            print(f'{n} frames', flush=True)
    p.stdin.close(); p.wait()
    return n


if __name__ == '__main__':
    print('frames:', run(sys.argv[1], sys.argv[2]))
