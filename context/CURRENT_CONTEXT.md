# CURRENT CONTEXT — Proton Peacock light-mode text-enlarge fix

**Halted:** 2026-07-10 by context-sentinel D41 RED hard-stop (~249,427/250,000 tokens).
**No image work was performed this session.** Only read `_imggen/NEXT_SESSION.md` and listed `_imggen/` dirs. Nothing changed on disk except this handoff + `_imggen/NEXT_SESSION.json`.

## The job (unchanged, not started)
Light-mode PDP feature images have TEXT TOO SMALL. The approved DARK originals in `_imggen/dark-backup/` have the correct, LARGER text (client enlarged for mobile legibility). Bring the 8 HTML rebuilds (`01,03,04,05,06,07,08,09`) UP to that size, and rebuild `02-foam-core` with fresh HTML text (its current version has a "whited-around" halo from recolored baked text).

Full step-by-step is in `_imggen/NEXT_SESSION.json` (steps 1–5) — read it first.

## Fast start for next session
1. Measure title + label cap-heights in `_imggen/dark-backup/01,02,06` (crop with PIL, Read the crops).
2. Enlarge `.title h1/.sub`, `.lab/.lab .sub`, loupe/callout label classes in `_imggen/base.css`; rebalance template positions; re-render 01,03,04,05,06,07,08,09.
3. Build text-free `_imggen/src/core-cutaway-plate.png` (largest connected component only) and new `02-foam-core.html` with fresh overlaid text.
4. View all 9 at full res vs dark-backup originals; contact sheet; iterate until clean.
5. Copy to `assets/peacock/NN.png`; recapture Desktop full-page proof; `open index.html`.

## Guardrails
- Branch `feat/light-mode`. Do NOT commit/push/switch branches.
- Abandon `recolor.py` / `recolor_02.py` — HTML rebuild only (per NEXT_SESSION.md verdict).
- Client is angry about being QA: self-review by VIEWING PIXELS, never claim clean unseen.
