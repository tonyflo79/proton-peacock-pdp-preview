#!/usr/bin/env python3
"""Process 5 client partner logos for the navy Our Partners band (#002855)."""
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage

SRC = "assets/partners/src"
OUT = "assets/partners"


def lum(arr):
    return 0.299 * arr[..., 0] + 0.587 * arr[..., 1] + 0.114 * arr[..., 2]


def autocrop(im, pad=6):
    a = np.array(im)[..., 3]
    ys, xs = np.where(a > 8)
    if len(xs) == 0:
        return im
    x0, x1 = xs.min(), xs.max()
    y0, y1 = ys.min(), ys.max()
    x0 = max(0, x0 - pad); y0 = max(0, y0 - pad)
    x1 = min(im.width - 1, x1 + pad); y1 = min(im.height - 1, y1 + pad)
    return im.crop((x0, y0, x1 + 1, y1 + 1))


def feather_alpha(alpha, erode_px=1, blur=0.8):
    """Erode opaque region slightly (kills dark rim) then blur for smooth edge."""
    a = Image.fromarray(alpha, "L")
    if erode_px:
        a = a.filter(ImageFilter.MinFilter(erode_px * 2 + 1))
    if blur:
        a = a.filter(ImageFilter.GaussianBlur(blur))
    return np.array(a)


def border_dark_knockout(rgb, dark_thresh, erode_px=1, blur=0.8):
    """Remove border-connected dark background via connected components."""
    l = lum(rgb)
    dark = l < dark_thresh
    lbl, n = ndimage.label(dark)
    border_ids = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
    border_ids.discard(0)
    bg = np.isin(lbl, list(border_ids))
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    alpha = feather_alpha(alpha, erode_px, blur)
    out = np.dstack([rgb, alpha]).astype(np.uint8)
    return Image.fromarray(out, "RGBA")


# 1) NFLPA — white bg knockout, recolor black wordmark -> white, keep red icon
def do_nflpa():
    im = Image.open(f"{SRC}/nflpa-official.png").convert("RGB")
    rgb = np.array(im).astype(np.int16)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    l = lum(rgb)
    # only remove border-connected white (keeps white line-art inside red icon)
    white = (r > 232) & (g > 232) & (b > 232)
    lbl, n = ndimage.label(white)
    border_ids = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
    border_ids.discard(0)
    bg = np.isin(lbl, list(border_ids))
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    # red icon = R clearly dominant
    is_red = (r - np.maximum(g, b) > 40) & (r > 90)
    # dark/black wordmark = low luminance and not red -> recolor to white
    dark_text = (l < 150) & (~is_red)
    out = rgb.copy()
    out[dark_text] = [255, 255, 255]
    # smooth alpha edge
    alpha = feather_alpha(alpha, erode_px=0, blur=0.6)
    rgba = np.dstack([out, alpha]).astype(np.uint8)
    im2 = autocrop(Image.fromarray(rgba, "RGBA"))
    im2.save(f"{OUT}/nflpa-white.png")
    print("nflpa-white.png", im2.size)


# 2) Elite Pickleball EP shield — solid black bg, metallic edges
def do_elite():
    im = Image.open(f"{SRC}/elite-pickleball-shield.jpeg").convert("RGB")
    rgb = np.array(im)
    out = border_dark_knockout(rgb, dark_thresh=45, erode_px=1, blur=1.0)
    out = autocrop(out)
    out.save(f"{OUT}/elite-pickleball.png")
    print("elite-pickleball.png", out.size)


# 3) The Picklr — white wordmark on solid black
def do_picklr():
    im = Image.open(f"{SRC}/the-picklr.png").convert("RGB")
    rgb = np.array(im).astype(np.float32)
    l = lum(rgb)
    # alpha ramps with luminance so white text stays crisp, black bg gone
    alpha = np.clip((l - 40) / (150 - 40) * 255, 0, 255).astype(np.uint8)
    # force wordmark pure white
    out = np.dstack([np.full_like(rgb, 255)[..., :3], alpha]).astype(np.uint8)
    im2 = autocrop(Image.fromarray(out, "RGBA"))
    im2.save(f"{OUT}/the-picklr.png")
    print("the-picklr.png", im2.size)


# 4) The Kitchen — keep green square, round corners, no knockout
def do_kitchen():
    im = Image.open(f"{SRC}/the-kitchen.jpg").convert("RGBA")
    w, h = im.size
    radius = int(min(w, h) * 0.09)
    mask = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=255)
    im.putalpha(mask)
    im.save(f"{OUT}/the-kitchen.png")
    print("the-kitchen.png", im.size)


# 5) MPO gold shield — dark gradient bg
def do_mpo():
    im = Image.open(f"{SRC}/mpo-shield.jpeg").convert("RGB")
    rgb = np.array(im)
    out = border_dark_knockout(rgb, dark_thresh=95, erode_px=1, blur=1.0)
    out = autocrop(out)
    out.save(f"{OUT}/mpo.png")
    print("mpo.png", out.size)


if __name__ == "__main__":
    do_nflpa()
    do_elite()
    do_picklr()
    do_kitchen()
    do_mpo()
