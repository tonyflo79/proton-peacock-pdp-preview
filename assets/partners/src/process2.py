#!/usr/bin/env python3
"""Round-2 partner logos (2026-07-28): Hunter's Games, Good Sport Foundation, Sparms, UDrippin.

Sources:
- sparms-seo.png            sparms.com Shopify CDN (white wordmark on black)
- udrippin-stacked-white.png udrippin.com CDN (white art on transparency)
- goodsport-foundation.jpg  globalpickleballfederation.org (colored logo on white)
- hunters-games-100.jpg     @huntersgamesaz IG profile pic, only 100px public ->
  hunters-games-2k.png      Higgsfield/bytedance 2k upscale of the above; circle-masked.
  NOTE: replace with the real vector/hi-res badge from Hunter's Games when Mike can source it.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = "assets/partners/src"
OUT = "assets/partners"


def autocrop(im, pad=6):
    a = np.array(im)[..., 3]
    ys, xs = np.where(a > 8)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    return im.crop((max(0, x0 - pad), max(0, y0 - pad),
                    min(im.width - 1, x1 + pad) + 1, min(im.height - 1, y1 + pad) + 1))


def do_sparms():  # white wordmark on solid black -> luminance alpha, force white
    rgb = np.array(Image.open(f"{SRC}/sparms-seo.png").convert("RGB")).astype(np.float32)
    l = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
    alpha = np.clip((l - 40) / (170 - 40) * 255, 0, 255).astype(np.uint8)
    out = np.dstack([np.full(rgb.shape, 255, np.uint8)[..., :3], alpha])
    autocrop(Image.fromarray(out, "RGBA")).save(f"{OUT}/sparms.png")


def do_udrippin():  # already white-on-transparent, crop + downsize
    im = autocrop(Image.open(f"{SRC}/udrippin-stacked-white.png").convert("RGBA"))
    im.thumbnail((1200, 1200), Image.LANCZOS)
    im.save(f"{OUT}/udrippin.png")


def do_goodsport():  # colored logo on white JPG -> white-matte removal, keeps teal/purple
    rgb = np.array(Image.open(f"{SRC}/goodsport-foundation.jpg").convert("RGB")).astype(np.float32)
    a = np.clip((255.0 - rgb.min(axis=-1)) * 1.35, 0, 255)
    c = np.clip((rgb - (255.0 - a[..., None])) / (np.maximum(a, 1e-4)[..., None] / 255.0), 0, 255)
    out = np.dstack([c.astype(np.uint8), a.astype(np.uint8)])
    autocrop(Image.fromarray(out, "RGBA")).save(f"{OUT}/good-sport.png")


def do_hunters():  # 2k-upscaled circular badge -> feathered circle mask
    im = Image.open(f"{SRC}/hunters-games-2k.png").convert("RGBA")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
    mask = Image.new("L", (s, s), 0)
    inset = int(s * 0.008)
    ImageDraw.Draw(mask).ellipse([inset, inset, s - 1 - inset, s - 1 - inset], fill=255)
    im.putalpha(mask.filter(ImageFilter.GaussianBlur(2)))
    im.thumbnail((900, 900), Image.LANCZOS)
    im.save(f"{OUT}/hunters-games.png")


if __name__ == "__main__":
    do_sparms()
    do_udrippin()
    do_goodsport()
    do_hunters()
