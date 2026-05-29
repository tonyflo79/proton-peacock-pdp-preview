# Proton Peacock PDP — Preview

High-fidelity dark-mode design preview for the Proton Sports Series Three
"Project Peacock" product detail page.

This is a **staging preview only** — a single self-contained `index.html`
(plain HTML/CSS + a little vanilla JS) for stakeholder review of layout,
typography, color, copy, and interactions. It is not production code; the
buy-box/selector CTAs are not wired to a real cart.

## Live preview

Served via GitHub Pages from `main` (root):
https://tonyflo79.github.io/proton-peacock-pdp-preview/

## Local preview

Open `index.html` directly in a browser. No build step. Fonts load from CDN
(Fontshare + Google Fonts), so an internet connection renders type correctly.

## Interactions

- **Hero gallery** — click any of the 9 thumbnails to swap the main header image.
- **Variant → header image** — clicking a **Shape** (Elongated / Wide-Body) or
  **Thickness** (13mm / 15mm) button — in the buy-box chips *or* the Configure
  selector cards — shows that SKU's image in the header and highlights its
  thumbnail. Shape also drives price ($195 Elongated / $175 Wide-Body). Default
  SKU: Wide-Body / 15mm.
- **FAQ** — single-open accordion.

## Files

| File | Purpose |
|---|---|
| `index.html` | The complete PDP — all CSS in a `<style>` block, interactive JS at the bottom |
| `assets/peacock/01–09…png` | Final approved square product renders (copy baked in — do not crop/re-render) |
| `assets/peacock/people/` | Pros, founder (`charles-darling.jpg`), and the construction/layup shot |
