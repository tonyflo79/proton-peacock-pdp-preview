#!/usr/bin/env python3
"""Build the text-free cutaway plate for Flamingo 02-foam-core.
Extract the ENTIRE client-approved paddle silhouette (honeycomb cutaway left half +
pink edge guard + branded right half + white handle) from the ORIGINAL DARK composite
as a transparent PNG (largest CC + fill-holes), strip the thin baked leader-line
appendages that stick out past the silhouette, and inpaint the baked pink/white leader
dots + horizontal line stubs that lie ON the paddle face. The cutaway is therefore
INSIDE the paddle by construction: the pink edge guard stays intact all the way round.

Input : src/fl-02-dark-src.png  (== HEAD:flamingo/assets/flamingo/pink/02-foam-core.png)
Output: src/fl-core-cutaway-plate.png  (transparent RGBA, paddle only, no baked leaders)

Reproducible: rerun from scratch each time (no incremental corruption)."""
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = 'src/fl-02-dark-src.png'
rgb = np.array(Image.open(SRC).convert('RGB'))
gray = np.array(Image.open(SRC).convert('L')).astype(np.float32)
R, G, B = rgb[:, :, 0].astype(np.int16), rgb[:, :, 1].astype(np.int16), rgb[:, :, 2].astype(np.int16)
H, W = gray.shape

# --- paddle silhouette = largest connected component of foreground ---
mask = gray > 30
lab, n = ndimage.label(mask)
sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
big = 1 + int(np.argmax(sizes))
paddle = ndimage.binary_fill_holes(lab == big)
paddle = ndimage.binary_fill_holes(ndimage.binary_closing(paddle, structure=np.ones((5, 5))))

# --- strip thin baked leader-line appendages that dangle off the silhouette ---
# (the label->dot lines lie over the black bg and touch the paddle edge, so they get
#  swept into the largest CC as ~2-6px protrusions). Morphological open + reconstruct
#  against the true paddle body removes anything thinner than the erosion radius while
#  keeping the paddle boundary (incl. handle + rounded corners) pixel-accurate.
core = ndimage.binary_erosion(paddle, iterations=5)
l2, m = ndimage.label(core)
s2 = ndimage.sum(np.ones_like(l2), l2, range(1, m + 1))
core = l2 == (1 + int(np.argmax(s2)))
paddle = ndimage.binary_dilation(core, iterations=5) & paddle

filled = rgb.copy()

# --- honeycomb-face artifacts: 3 baked leaders that lie ON the hex cutaway -----------
# 1) edge-guard dot + short stub  (~680,228)
# 2) polypropylene-honeycomb dot + long horizontal line across the hexes (~y500)
# 3) solid-foam-core dot + long horizontal line across the hexes (~y757)
# The honeycomb repeats with a vertical period of 66px (measured by autocorrelation),
# so copying each artifact pixel from exactly +-66px (phase-locked) rebuilds the hexes.
PER = 66
boxes = [
    (640, 700, 214, 242),   # edge-guard dot + stub
    (640, 918, 490, 512),   # honeycomb dot + horizontal line
    (640, 918, 747, 769),   # foam-core dot + horizontal line
]
art = np.zeros(gray.shape, bool)
bright = gray > 90
pink = (R > 150) & (G < 140) & (B > 60)
for x0, x1, y0, y1 in boxes:
    b = np.zeros(gray.shape, bool)
    b[y0:y1, x0:x1] = True
    art |= b & (bright | pink)
art = ndimage.binary_dilation(art, iterations=2) & paddle
# never touch the branded right half / seam
art[:, 1000:] = False

todo = art.copy()
ys, xs = np.where(todo)
for k in range(1, 9):
    for d in (1, -1):
        if len(ys) == 0:
            break
        sy = np.clip(ys + d * k * PER, 0, H - 1)
        good = paddle[sy, xs] & ~art[sy, xs]     # source must be on-paddle & clean
        idx = np.where(good)[0]
        filled[ys[idx], xs[idx]] = filled[sy[idx], xs[idx]]
        todo[ys[idx], xs[idx]] = False
        ys, xs = np.where(todo)

# --- handle dot (~1023,1423): nearest-opaque-non-artifact inpaint (uniform grip) -----
hart = np.zeros(gray.shape, bool)
hart[1405:1443, 1004:1044] = True
hart &= paddle
invalid = hart | (~paddle)
ind = ndimage.distance_transform_edt(invalid, return_distances=False, return_indices=True)
ys, xs = np.where(hart)
filled[ys, xs] = filled[ind[0][ys, xs], ind[1][ys, xs]]

# --- alpha: erode 2px to drop black-blended fringe, feather 0.8px --------------------
edge = ndimage.binary_erosion(paddle, iterations=2)
alpha = ndimage.gaussian_filter(edge.astype(np.float32), 0.8)
alpha = np.clip(alpha * 255, 0, 255).astype(np.uint8)
Image.fromarray(np.dstack([filled, alpha]), 'RGBA').save('src/fl-core-cutaway-plate.png')
print('wrote src/fl-core-cutaway-plate.png  paddle px', int(paddle.sum()),
      'bbox x', np.where(paddle.any(0))[0][[0, -1]], 'y', np.where(paddle.any(1))[0][[0, -1]])
