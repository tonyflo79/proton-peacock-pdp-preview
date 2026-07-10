#!/usr/bin/env python3
"""
Conservative recolor of 02-foam-core (dark -> light).
SAFE ONLY for this image: no zoom loupe, bright rim fully encloses the paddle,
so a border-connected black flood cannot leak into the silhouette.

DOES ONLY THREE THINGS:
  1. background near-black (connected to border) -> soft white studio gradient
  2. exterior text: white-ish -> dark ink, cyan-ish -> brand blue
  3. letter counters (enclosed black holes in that exterior text) -> white gradient

Everything inside the paddle silhouette is left byte-for-byte identical.
"""
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = "_imggen/dark-backup/02-foam-core.png"
OUT = "_imggen/out/02-foam-core-light.png"

INK  = np.array([0x14, 0x16, 0x1C], dtype=np.uint8)   # dark text
BLUE = np.array([0x2F, 0x6F, 0xE0], dtype=np.uint8)   # brand blue

img = np.asarray(Image.open(SRC).convert("RGB")).astype(np.int16)
H, W, _ = img.shape
R, G, B = img[..., 0], img[..., 1], img[..., 2]
mx = img.max(axis=2)
mn = img.min(axis=2)

# ---- 1. background: near-black AND connected to the image border ----------
nearblack = mx < 40
lbl, n = ndimage.label(nearblack)
border_labels = set(np.unique(lbl[0, :])) | set(np.unique(lbl[-1, :])) \
              | set(np.unique(lbl[:, 0])) | set(np.unique(lbl[:, -1]))
border_labels.discard(0)
bg = np.isin(lbl, list(border_labels))

# soft white radial studio gradient: #FFF center -> #F2F3F5 edge
yy, xx = np.mgrid[0:H, 0:W]
cy, cx = (H - 1) / 2.0, (W - 1) / 2.0
dist = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
t = (dist / dist.max())[..., None]                      # 0 center .. 1 corner
c0 = np.array([255, 255, 255], dtype=np.float32)
c1 = np.array([0xF2, 0xF3, 0xF5], dtype=np.float32)
grad = (c0 * (1 - t) + c1 * t).astype(np.uint8)          # (H,W,3)

# ---- 2. exterior text masks (computed on ORIGINAL pixels) -----------------
sat = mx - mn
whiteish = (mn > 150) & (sat < 40)
cyanish  = (G > 140) & (B > 140) & (R < 130)

near_bg = ndimage.binary_dilation(bg, iterations=7)
ext_white = whiteish & near_bg
ext_cyan  = cyanish  & near_bg

# ---- 3. letter counters (enclosed holes) -> white gradient ----------------
ink_mask = ext_white | ext_cyan
filled = ndimage.binary_fill_holes(ndimage.binary_dilation(ink_mask, iterations=4))
counters = filled & ~ink_mask

# ---- compose (order matters: bg, then text, then counters) ----------------
out = img.astype(np.uint8).copy()
out[bg]        = grad[bg]
out[ext_white] = INK
out[ext_cyan]  = BLUE
out[counters]  = grad[counters]

Image.fromarray(out).save(OUT)
print("saved", OUT)
print("bg px           :", int(bg.sum()))
print("ext_white px    :", int(ext_white.sum()))
print("ext_cyan px     :", int(ext_cyan.sum()))
print("counter px      :", int(counters.sum()))
