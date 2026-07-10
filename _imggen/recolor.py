#!/usr/bin/env python3
"""Recolor an approved DARK feature composite to LIGHT mode.
Identical composition & text — only color changes:
  - pure-black background  -> soft white studio gradient
  - exterior white callout text / lines -> dark ink
  - exterior cyan subtitle / leaders     -> brand blue
The paddle + all AI elements (loupe zooms, core cutaway, seal, dots) are untouched.
Usage: recolor.py in.png out.png
"""
import sys, numpy as np
from PIL import Image
from scipy import ndimage

INK  = (18, 20, 26)      # exterior white text -> dark ink
BLUE = (47, 111, 224)    # exterior cyan  -> brand blue

def main(inp, outp):
    im = Image.open(inp).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    H, W, _ = a.shape
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    mx = a.max(2); mn = a.min(2)

    sat = (mx - mn)
    # 1) exterior background = near-black region connected to the image border
    near_black = mx < 40
    lbl, n = ndimage.label(near_black)
    border = set(np.unique(np.concatenate([lbl[0], lbl[-1], lbl[:,0], lbl[:,-1]])))
    border.discard(0)
    bg = np.isin(lbl, list(border))
    bg_dil = ndimage.binary_dilation(bg, iterations=7)

    # 2) exterior graphics (text/lines) = white-ish or cyan-ish, adjacent to background
    whiteish = (mn > 150) & (sat < 55)
    cyanish  = (G > 150) & (B > 150) & (R < 165) & ((G - R) > 25)
    ext_white = whiteish & bg_dil & ~bg
    ext_cyan  = cyanish  & bg_dil & ~bg
    # 2b) leftover exterior anti-alias halo (grey fringe around glyphs + paddle edge) -> erase to bg
    halo = bg_dil & ~bg & ~ext_white & ~ext_cyan & (mx < 175)
    # 2c) letter counters: regions enclosed by ink text (holes in D,P,O,R,A,e,o,a...).
    # Close hairline anti-alias gaps in the outline first so the WHOLE counter fills (not just its rim).
    ink = ext_white | ext_cyan
    ink_closed = ndimage.binary_dilation(ink, iterations=4)
    counters = ndimage.binary_fill_holes(ink_closed) & ~ink

    # 3) soft white studio gradient for the background
    yy, xx = np.mgrid[0:H, 0:W]
    cx, cy = W*0.5, H*0.42
    d = np.sqrt(((xx-cx)/(W*0.62))**2 + ((yy-cy)/(H*0.62))**2)
    t = np.clip(d, 0, 1)
    grad = (255 - t*13)[..., None] * np.ones(3)          # #FFF center -> ~#F2F3F5 edge
    grad[..., 2] += 2                                     # a hair cooler
    grad = np.clip(grad, 0, 255)

    out = a.astype(np.float32).copy()
    out[bg]       = grad[bg]
    out[halo]     = grad[halo]
    out[counters] = grad[counters]
    out[ext_white] = INK
    out[ext_cyan]  = BLUE
    Image.fromarray(np.clip(out,0,255).astype(np.uint8)).save(outp)
    print(f"{inp} -> {outp}  bg%={bg.mean()*100:.1f} white_px={ext_white.sum()} cyan_px={ext_cyan.sum()}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
