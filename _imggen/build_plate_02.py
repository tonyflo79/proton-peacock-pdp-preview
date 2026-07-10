#!/usr/bin/env python3
"""Build the text-free cutaway plate for 02-foam-core.
Extract the paddle silhouette from dark-backup/02-foam-core.png (largest CC),
erase all baked leader nodes/lines, output transparent PNG src/core-cutaway-plate.png.
Reproducible: rerun from scratch each time (no incremental corruption)."""
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = 'dark-backup/02-foam-core.png'
rgb = np.array(Image.open(SRC).convert('RGB'))
gray = np.array(Image.open(SRC).convert('L'))

# --- paddle silhouette = largest connected component of foreground ---
mask = gray > 30
lab, n = ndimage.label(mask)
sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
big = 1 + int(np.argmax(sizes))
paddle = ndimage.binary_fill_holes(lab == big)
paddle = ndimage.binary_fill_holes(ndimage.binary_closing(paddle, structure=np.ones((5, 5))))

filled = rgb.copy()

# --- 2 mid left-edge nodes: vertical directional sampling (preserves gold|white|core bands) ---
for cx, cy, d in [(752, 455, -1), (912, 697, -1)]:
    art = np.zeros(gray.shape, bool)
    art[cy - 22:cy + 22, cx - 24:cx + 24] = True
    art[cy - 7:cy + 8, 585:cx + 24] = True
    art &= paddle
    ys, xs = np.where(art)
    for step in [46, 92, 138, 184, 230]:
        if len(ys) == 0:
            break
        sy = np.clip(ys + d * step, 0, 2047)
        good = ~art[sy, xs]
        idx = np.where(good)[0]
        filled[ys[idx], xs[idx]] = filled[sy[idx], xs[idx]]
        art[ys[idx], xs[idx]] = False
        ys, xs = np.where(art)

# --- top corner node (710,228): straddles white band + rounded core corner.
# Reconstruct by classifying each pixel band via a right-neighbour probe. ---
WHITE = np.array([248, 247, 246], np.uint8)
gyf = np.array(Image.fromarray(filled).convert('L'))
Rf, Gf, Bf = filled[:, :, 0].astype(np.int16), filled[:, :, 1].astype(np.int16), filled[:, :, 2].astype(np.int16)
teal = (Bf > 110) & (Gf > 110) & (Rf < 120)  # bright teal ring pixels
# also clear the leader stub band to the left of the node
for yy in range(150, 300):
    for xx in range(586, 750):
        if not paddle[yy, xx]:
            continue
        if gyf[yy, xx] < 175 or teal[yy, xx]:  # dark OR teal fragment (node ring / leader line)
            # probe 18px right: bright => on white band; else => core edge
            rx = min(xx + 18, 2047)
            if gyf[yy, rx] > 185:
                filled[yy, xx] = WHITE
            else:
                filled[yy, xx] = filled[yy, min(xx + 42, 2047)]  # deep core grey

# --- white-band ghost pass: whiten the band up to the core edge, per row ---
gyf = np.array(Image.fromarray(filled).convert('L'))
for yy in range(186, 270):
    # find core left edge in this row (first sustained dark-grey pixel scanning right)
    core_left = None
    for xx in range(702, 772):
        if gyf[yy, xx] < 100 and gyf[yy, xx + 3] < 100:
            core_left = xx
            break
    if core_left is None:
        continue
    for xx in range(698, core_left - 1):
        if gyf[yy, xx] < 236:          # anything dimmer than clean white band = ghost
            filled[yy, xx] = WHITE

# --- 2 handle nodes: nearest-opaque-non-artifact inpaint (uniform purple grip) ---
art = np.zeros(gray.shape, bool)
for cx, cy in [(1023, 1422), (1023, 1462)]:
    art[cy - 16:cy + 16, cx - 18:cx + 20] = True
art &= paddle
invalid = art | (~paddle)
ind = ndimage.distance_transform_edt(invalid, return_distances=False, return_indices=True)
ys, xs = np.where(art)
filled[ys, xs] = filled[ind[0][ys, xs], ind[1][ys, xs]]

# --- alpha: erode 2px to drop black-blended fringe, feather 0.8px ---
core = ndimage.binary_erosion(paddle, iterations=2)
alpha = ndimage.gaussian_filter(core.astype(np.float32), 0.8)
alpha = np.clip(alpha * 255, 0, 255).astype(np.uint8)
Image.fromarray(np.dstack([filled, alpha]), 'RGBA').save('src/core-cutaway-plate.png')
print('wrote src/core-cutaway-plate.png')
