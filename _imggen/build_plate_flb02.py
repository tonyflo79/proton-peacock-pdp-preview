#!/usr/bin/env python3
"""Build the text-free cutaway plate for Flamingo BLUE 02-foam-core.
Extract the ENTIRE client-approved paddle silhouette (honeycomb cutaway left half +
blue edge guard + branded right half + pink handle) from the ORIGINAL DARK blue
composite as a transparent PNG (largest CC + fill-holes), strip the thin baked
leader-line appendages that stick out past the silhouette, and inpaint the baked
pink-ring leader dots + horizontal line stubs that lie ON the paddle face. The
cutaway is therefore INSIDE the paddle by construction: the blue edge guard stays
intact all the way round.

Geometry/box coords verified identical to the pink Flamingo 02 source (same
template, colorway swap only) via pixel inspection: leader-dot ring color is the
same [255,111,165] pink at the same (680,228)/(902,498)/(902,757)/(1023,1420) spots.

Input : ../flamingo/assets/flamingo/blue/02-foam-core.png (still dark on disk)
Output: src/flb-core-cutaway-plate.png  (transparent RGBA, paddle only, no baked leaders)

Reproducible: rerun from scratch each time (no incremental corruption)."""
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = '../flamingo/assets/flamingo/blue/02-foam-core.png'
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
# 1) edge-guard dot + short stub  (~680,228) -- straddles the curved white edge-guard
#    band / dark-hex boundary, so it gets its own nearest-neighbour inpaint below
#    (a fixed +-66px vertical copy would cross the curve and bite a notch out of the
#    white band, since the band width isn't constant along the curve).
# 2) polypropylene-honeycomb dot + long horizontal line across the hexes (~y500)
# 3) solid-foam-core dot + long horizontal line across the hexes (~y757)
# Boxes 2 and 3 sit entirely inside the flat hex field (no boundary), so the honeycomb's
# vertical repeat period of 66px (measured by autocorrelation) lets phase-locked +-66px
# copies rebuild the hexes cleanly.
PER = 66
bright = gray > 90
pink = (R > 150) & (G < 140) & (B > 60)   # leader-dot ring color is pink on every colorway

# -- box 0: edge-guard dot/stub -> boundary-aware reconstruction ----------------------
# This dot sits ON the curved white edge-guard band / dark-hex boundary. A naive
# nearest-neighbour or fixed-offset copy crosses the curve and either bites a notch out
# of the band or warps the hex-grid lines. Instead: per row, split the artifact into a
# "band" part (filled flat with the measured band colour) and a "hex" part (filled via
# the same phase-locked +-66px vertical copy used below), using the actual paddle-mask
# left edge per row (reliable even inside the artifact) plus a band-width measured from
# clean rows just outside the artifact and linearly interpolated across it.
BAND = np.array([226, 226, 230], np.uint8)
edge_art = np.zeros(gray.shape, bool)
edge_art[204:250, 636:706] = True
edge_art &= paddle & (bright | pink)
edge_art = ndimage.binary_dilation(edge_art, iterations=2) & paddle
edge_art[:, 700:] = False  # never eat into the hex field beyond the measured band+margin

paddle_left = np.array([np.where(paddle[yy])[0][0] if paddle[yy].any() else -1 for yy in range(H)])


def band_width_at(yy):
    """Measure band width (paddle-left -> first sustained-dark run) on a clean row."""
    left = paddle_left[yy]
    if left < 0:
        return 11
    for xx in range(left, left + 40):
        if gray[yy, xx] < 100 and gray[yy, xx + 2] < 100 and gray[yy, xx + 4] < 100:
            return xx - left
    return 11


bw_top = band_width_at(200)    # clean row just above the artifact
bw_bot = band_width_at(252)    # clean row just below the artifact
for yy in range(204, 250):
    left = paddle_left[yy]
    if left < 0:
        continue
    bw = bw_top + (bw_bot - bw_top) * (yy - 200) / (252 - 200)
    band_end = int(round(left + bw))
    row_art = np.where(edge_art[yy])[0]
    if len(row_art) == 0:
        continue
    band_px = row_art[row_art < band_end]
    hex_px = row_art[row_art >= band_end]
    if len(band_px):
        filled[yy, band_px] = BAND
    if len(hex_px):
        # two-pass phase-locked fill: try +66 first, fall back to -66 for any leftovers
        remaining = hex_px.copy()
        for d in (1, -1):
            if len(remaining) == 0:
                break
            sy = np.clip(yy + d * 66, 0, H - 1)
            ok = paddle[sy, remaining] & ~edge_art[sy, remaining]
            filled[yy, remaining[ok]] = filled[sy, remaining[ok]]
            remaining = remaining[~ok]

# -- boxes 1/2: honeycomb + foam-core dots/lines -> phase-locked hex copy --------------
boxes = [
    (640, 918, 490, 512),   # honeycomb dot + horizontal line
    (640, 918, 747, 769),   # foam-core dot + horizontal line
]
art = np.zeros(gray.shape, bool)
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

# --- handle dot + line stub (~1023,1424): nearest-opaque-non-artifact inpaint (uniform
# pink grip). Box widened left to 955 (paddle edge is ~970 here) because the baked
# leader LINE runs from the label all the way to the dot at y~1424-1425, not just the
# dot ring itself (measured: white line px range x[970,1031] @ y1424-1425). --
hart = np.zeros(gray.shape, bool)
hart[1410:1438, 955:1044] = True
hart &= paddle
invalid = hart | (~paddle)
ind = ndimage.distance_transform_edt(invalid, return_distances=False, return_indices=True)
ys, xs = np.where(hart)
filled[ys, xs] = filled[ind[0][ys, xs], ind[1][ys, xs]]

# --- alpha: erode 2px to drop black-blended fringe, feather 0.8px --------------------
edge = ndimage.binary_erosion(paddle, iterations=2)
alpha = ndimage.gaussian_filter(edge.astype(np.float32), 0.8)
alpha = np.clip(alpha * 255, 0, 255).astype(np.uint8)
Image.fromarray(np.dstack([filled, alpha]), 'RGBA').save('src/flb-core-cutaway-plate.png')
print('wrote src/flb-core-cutaway-plate.png  paddle px', int(paddle.sum()),
      'bbox x', np.where(paddle.any(0))[0][[0, -1]], 'y', np.where(paddle.any(1))[0][[0, -1]])
