"""
J.A.R.V.I.S. style holographic hand interface (MediaPipe Tasks API, Python 3.13 OK).

Install:
    pip install --upgrade opencv-python mediapipe numpy

Run:
    python jarvis_hologram.py

Gestures:
    Pinch (thumb + index) near the hologram  -> grab it and drag it around
    Drag while pinching                        -> spin it
    Pinch with BOTH hands                      -> pull apart / push together to scale,
                                                  twist your hands to rotate (the Stark move)
    Open palm                                  -> arc-reactor ring spins on your palm

Keys:
    b = toggle camera background | r = reset hologram | q / ESC = quit
"""

import math
import os
import time
import urllib.request

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_NAME = "hand_landmarker.task"
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
             "hand_landmarker/float16/1/hand_landmarker.task")

# BGR colours
CYAN = (255, 225, 60)
DIM = (150, 105, 15)
ORANGE = (40, 150, 255)
WHITE = (255, 255, 255)
FONT = cv2.FONT_HERSHEY_SIMPLEX

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20),
    (0, 17),
]
FINGERTIPS = [4, 8, 12, 16, 20]


# ------------------------------------------------------------------ helpers
def ensure_model():
    path = os.path.join(HERE, MODEL_NAME)
    if not os.path.exists(path):
        print("Downloading hand model ...")
        urllib.request.urlretrieve(MODEL_URL, path)
    return path


def ip(p):
    return int(p[0]), int(p[1])


def txt(layer, s, org, scale=0.45, color=CYAN, thick=1):
    cv2.putText(layer, s, ip(org), FONT, scale, color, thick, cv2.LINE_AA)


def rot_matrix(rx, ry, rz):
    cx, sx = math.cos(rx), math.sin(rx)
    cy, sy = math.cos(ry), math.sin(ry)
    cz, sz = math.cos(rz), math.sin(rz)
    Rx = np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]])
    Ry = np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]])
    Rz = np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])
    return Rz @ Ry @ Rx


def make_icosahedron():
    phi = (1 + 5 ** 0.5) / 2
    v = []
    for a in (-1, 1):
        for b in (-phi, phi):
            v += [(0, a, b), (a, b, 0), (b, 0, a)]
    v = np.array(v, float)
    v /= np.linalg.norm(v[0])
    dists = [np.linalg.norm(v[i] - v[j]) for i in range(12) for j in range(i + 1, 12)]
    edge = min(dists)
    edges = [(i, j) for i in range(12) for j in range(i + 1, 12)
             if np.linalg.norm(v[i] - v[j]) < edge * 1.01]
    return v, edges


ICO_V, ICO_E = make_icosahedron()


class Holo:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.reset()

    def reset(self):
        self.c = np.array([self.w / 2, self.h / 2], float)
        self.scale = min(self.w, self.h) * 0.17
        self.rx, self.ry, self.rz = 0.5, 0.0, 0.0


def draw_wire(layer, verts, edges, c, scale, color, thick=1):
    s = scale * (1 + 0.2 * verts[:, 2])
    px = c[0] + verts[:, 0] * s
    py = c[1] + verts[:, 1] * s
    for i, j in edges:
        cv2.line(layer, (int(px[i]), int(py[i])), (int(px[j]), int(py[j])),
                 color, thick, cv2.LINE_AA)
    for x, y in zip(px, py):
        cv2.circle(layer, (int(x), int(y)), 3, WHITE, -1, cv2.LINE_AA)


def draw_ticks(layer, c, r, length, count, offset, color):
    for k in range(count):
        a = offset + k * 2 * math.pi / count
        p1 = (c[0] + math.cos(a) * r, c[1] + math.sin(a) * r)
        p2 = (c[0] + math.cos(a) * (r + length), c[1] + math.sin(a) * (r + length))
        cv2.line(layer, ip(p1), ip(p2), color, 1, cv2.LINE_AA)


def draw_hologram(layer, obj, t, color):
    R = rot_matrix(obj.rx, obj.ry, obj.rz)
    draw_wire(layer, ICO_V @ R.T, ICO_E, obj.c, obj.scale, color, 1)

    R2 = rot_matrix(-obj.rx * 1.3, -obj.ry * 1.6, -obj.rz)
    draw_wire(layer, (ICO_V * 0.5) @ R2.T, ICO_E, obj.c, obj.scale, DIM, 1)

    cv2.circle(layer, ip(obj.c), max(3, int(obj.scale * 0.12)), WHITE, -1, cv2.LINE_AA)

    # orbit rings
    c = ip(obj.c)
    r = int(obj.scale * 1.45)
    for k, ang in enumerate((0, 60, 120)):
        cv2.ellipse(layer, c, (r, max(2, int(r * 0.32))), ang + t * 15, 0, 360,
                    DIM, 1, cv2.LINE_AA)
    # outer HUD ring
    cv2.circle(layer, c, int(obj.scale * 1.75), DIM, 1, cv2.LINE_AA)
    draw_ticks(layer, obj.c, obj.scale * 1.75, 8, 72, -t * 0.3, DIM)
    for k in range(3):
        a0 = t * 70 + k * 120
        cv2.ellipse(layer, c, (int(obj.scale * 1.9),) * 2, 0, a0, a0 + 50,
                    color, 2, cv2.LINE_AA)
    txt(layer, f"SCALE {obj.scale / min(obj.w, obj.h) * 100:4.0f}%",
        (obj.c[0] + obj.scale * 1.2, obj.c[1] + obj.scale * 2.05), 0.4, color)


def draw_hud_circle(layer, c, r, t):
    cv2.circle(layer, c, r, CYAN, 1, cv2.LINE_AA)
    cv2.circle(layer, c, r - 14, DIM, 1, cv2.LINE_AA)
    cv2.circle(layer, c, 6, CYAN, -1, cv2.LINE_AA)
    draw_ticks(layer, c, r, 7, 60, t * 0.5, CYAN)
    for k in range(3):
        a0 = -t * 90 + k * 120
        cv2.ellipse(layer, c, (r - 14, r - 14), 0, a0, a0 + 60, CYAN, 3, cv2.LINE_AA)
    for k in range(4):
        a0 = t * 140 + k * 90
        cv2.ellipse(layer, c, (r - 28, r - 28), 0, a0, a0 + 25, ORANGE, 2, cv2.LINE_AA)


def corner_brackets(layer, w, h, m=20, ln=40):
    for (x, y, dx, dy) in ((m, m, 1, 1), (w - m, m, -1, 1),
                           (m, h - m, 1, -1), (w - m, h - m, -1, -1)):
        cv2.line(layer, (x, y), (x + dx * ln, y), CYAN, 2, cv2.LINE_AA)
        cv2.line(layer, (x, y), (x, y + dy * ln), CYAN, 2, cv2.LINE_AA)


def draw_hand(layer, pts, label, t, pinching):
    for a, b in HAND_CONNECTIONS:
        cv2.line(layer, ip(pts[a]), ip(pts[b]), CYAN, 2, cv2.LINE_AA)
    for p in pts:
        cv2.circle(layer, ip(p), 3, WHITE, -1, cv2.LINE_AA)
    for idx in FINGERTIPS:
        col = ORANGE if pinching else CYAN
        cv2.circle(layer, ip(pts[idx]), 11, col, 1, cv2.LINE_AA)
    # faint web from palm to fingertips
    for idx in FINGERTIPS:
        cv2.line(layer, ip(pts[9]), ip(pts[idx]), DIM, 1, cv2.LINE_AA)

    palm = np.linalg.norm(pts[0] - pts[9]) + 1e-6
    centre = (pts[0] + pts[9]) / 2
    r = int(palm * 0.6)
    is_open = all(pts[tip][1] < pts[pip][1]
                  for tip, pip in zip((8, 12, 16, 20), (6, 10, 14, 18)))
    c = ip(centre)
    if is_open:  # arc reactor palm ring
        cv2.circle(layer, c, r, CYAN, 1, cv2.LINE_AA)
        cv2.circle(layer, c, int(r * 0.7), DIM, 1, cv2.LINE_AA)
        for k in range(3):
            a0 = t * 150 + k * 120
            cv2.ellipse(layer, c, (r, r), 0, a0, a0 + 70, CYAN, 3, cv2.LINE_AA)
        for k in range(3):
            a0 = -t * 200 + k * 120
            cv2.ellipse(layer, c, (int(r * 0.7),) * 2, 0, a0, a0 + 40,
                        ORANGE, 2, cv2.LINE_AA)
        cv2.circle(layer, c, max(3, int(r * 0.22)), WHITE, -1, cv2.LINE_AA)
    else:
        cv2.circle(layer, c, int(r * 0.5), DIM, 1, cv2.LINE_AA)

    # label near wrist
    w0 = pts[0]
    cv2.line(layer, ip(w0), ip(w0 + np.array([50, 40])), CYAN, 1, cv2.LINE_AA)
    txt(layer, f"{label.upper()}_HAND // LOCKED", w0 + np.array([55, 40]), 0.4)
    txt(layer, f"X:{int(w0[0]):04d} Y:{int(w0[1]):04d}", w0 + np.array([55, 56]), 0.38, DIM)


# --------------------------------------------------------------------- main
def main():
    options = vision.HandLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=ensure_model()),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
    )

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open the camera. Check Windows camera privacy settings.")
        return

    ok, frame = cap.read()
    if not ok:
        print("Failed to read from camera.")
        return
    h, w, _ = frame.shape

    # static grid overlay
    grid = np.zeros((h, w, 3), np.uint8)
    for x in range(0, w, 60):
        cv2.line(grid, (x, 0), (x, h), (45, 28, 0), 1)
    for y in range(0, h, 60):
        cv2.line(grid, (0, y), (w, y), (45, 28, 0), 1)

    obj = Holo(w, h)
    show_cam = True
    pinching = {}
    grabbed_by = None
    offset = np.zeros(2)
    last_p = np.zeros(2)
    ref = (1, 1, 0, 0)
    fps = 30.0
    prev = time.time()
    start = prev

    with vision.HandLandmarker.create_from_options(options) as hands:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Failed to read from camera.")
                break
            frame = cv2.flip(frame, 1)

            now = time.time()
            t = now - start
            fps = 0.9 * fps + 0.1 / max(now - prev, 1e-6)
            prev = now

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.detect_for_video(
                mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb), int(t * 1000))

            # ---- collect hands + pinch state (with hysteresis) ----
            hands_pts, pinch_pt = {}, {}
            for i, lm in enumerate(result.hand_landmarks or []):
                label = result.handedness[i][0].category_name
                pts = np.array([(p.x * w, p.y * h) for p in lm])
                hands_pts[label] = pts
                palm = np.linalg.norm(pts[0] - pts[9]) + 1e-6
                pd = np.linalg.norm(pts[4] - pts[8])
                was = pinching.get(label, False)
                pinching[label] = pd < (0.55 if was else 0.33) * palm
                pinch_pt[label] = (pts[4] + pts[8]) / 2
            for label in list(pinching):
                if label not in hands_pts:
                    pinching[label] = False

            active = [l for l in hands_pts if pinching.get(l)]

            # ---- grab / scale / rotate logic ----
            if len(active) == 2:
                a, b = pinch_pt[active[0]], pinch_pt[active[1]]
                mid = (a + b) / 2
                d = max(np.linalg.norm(b - a), 1.0)
                ang = math.atan2(b[1] - a[1], b[0] - a[0])
                if grabbed_by != "both":
                    grabbed_by = "both"
                    ref = (d, obj.scale, ang, obj.rz)
                d0, s0, a0, rz0 = ref
                target_s = float(np.clip(s0 * d / d0, 35, min(w, h) * 0.42))
                obj.scale += (target_s - obj.scale) * 0.35
                obj.rz += ((rz0 + (ang - a0)) - obj.rz) * 0.35
                obj.c += (mid - obj.c) * 0.4
            elif len(active) == 1:
                l = active[0]
                p = pinch_pt[l]
                if grabbed_by == l:
                    obj.c += ((p + offset) - obj.c) * 0.5
                    dlt = p - last_p
                    obj.ry += dlt[0] * 0.012
                    obj.rx -= dlt[1] * 0.012
                elif np.linalg.norm(p - obj.c) < obj.scale * 1.5:
                    grabbed_by = l
                    offset = obj.c - p
                else:
                    grabbed_by = None
                last_p = p.copy()
            else:
                grabbed_by = None

            obj.ry += 0.012 if grabbed_by is None else 0.002
            obj.rx += 0.003 if grabbed_by is None else 0.0

            # ---- draw everything on a glow layer ----
            layer = np.zeros((h, w, 3), np.uint8)
            corner_brackets(layer, w, h)
            draw_hologram(layer, obj, t, ORANGE if grabbed_by else CYAN)

            for label, pts in hands_pts.items():
                draw_hand(layer, pts, label, t, pinching.get(label, False))
                if pinching.get(label):
                    pp = pinch_pt[label]
                    cv2.circle(layer, ip(pp), 16, ORANGE, 2, cv2.LINE_AA)
                    txt(layer, "GRAB", pp + np.array([20, -10]), 0.45, ORANGE, 1)
                    if grabbed_by in (label, "both"):
                        cv2.line(layer, ip(pp), ip(obj.c), ORANGE, 1, cv2.LINE_AA)

            # HUD text + widgets
            txt(layer, "J.A.R.V.I.S  //  ONLINE", (40, 50), 0.65, CYAN, 2)
            txt(layer, f"HANDS DETECTED: {len(hands_pts)}   FPS: {fps:4.1f}", (40, 75), 0.45)
            status = "OBJECT GRABBED" if grabbed_by else "SCANNING..."
            txt(layer, f"STATUS: {status}", (40, 96), 0.45, ORANGE if grabbed_by else DIM)
            draw_hud_circle(layer, (w - 95, 100), 60, t)
            for k in range(14):
                bh = int(8 + 26 * abs(math.sin(t * 2 + k * 0.6)))
                cv2.rectangle(layer, (40 + k * 9, h - 45 - bh), (46 + k * 9, h - 45),
                              DIM, -1)
            txt(layer, "PINCH: GRAB | 2 HANDS: SCALE+ROTATE | B: BG | R: RESET | Q: QUIT",
                (w // 2 - 270, h - 22), 0.42, DIM)

            # ---- compose ----
            if show_cam:
                g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)
                base = np.dstack([g * 0.55, g * 0.38, g * 0.12]).astype(np.uint8)
                base[::3] = (base[::3] * 0.55).astype(np.uint8)  # scanlines
            else:
                base = np.zeros_like(frame)

            out = cv2.add(cv2.add(base, grid), layer)
            glow = cv2.GaussianBlur(layer, (0, 0), 10)
            out = cv2.add(out, glow)

            cv2.imshow("JARVIS Hologram", out)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27):
                break
            elif key == ord("b"):
                show_cam = not show_cam
            elif key == ord("r"):
                obj.reset()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()