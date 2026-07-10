# Proton Peacock repo — CURRENT CONTEXT (2026-07-11)

## Just shipped (committed + pushed, branch `feat/light-mode`, commit 516088e)
Light-mode **feature images** finished: on-image text enlarged to match the approved dark
originals (titles cap~70px/font 103, hero subtitles 01+02 font 70, feature subtitles font 47,
01 labels font 48, 02 labels UPPERCASE font 40 — set in `_imggen/base.css`). **02-foam-core
rebuilt** from a text-free cutaway plate (`_imggen/build_plate_02.py` → `src/core-cutaway-plate.png`)
with fresh HTML overlays, no baked-text halo. All 9 installed to `assets/peacock/NN.png`; Desktop
proof `proton-peacock-lightmode-FULLPAGE.png` (1440×9200) re-saved. `index.html` (Peacock PDP) is
light and current. NOT merged — merge is Anthony's.

## NEXT (do this in a FRESH session — this one hit context ORANGE)
**Build the net-new light PROTON HOMEPAGE as `home.html`.** Full spec + copy + structure +
image sources + messaging canon in **`context/HOMEPAGE-BUILD-HANDOFF.json`** — read that first.

Key locked decisions:
- 3 tiers: **umbrella hero** (shared aerospace DNA) → **the paddles** (Peacock/Flamingo/Roadrunner,
  each its own core+character) → **rest of Proton** (AeroGrade story, pros, founder+cert, FAQ, close).
- Hero (LOCKED by Anthony): H1 "Aerospace-grade carbon fiber. Roughness-enhanced spin." /
  subhead "With a high-performance core tuned to your game." / CTA "Find your paddle →" /
  strip "Carbon Fiber Face · Optimized Spin · UPA + USA Pickleball Certified". No core name /
  no warranty claim in the hero (those are paddle-specific).
- Reuse `index.html`'s light design system verbatim.

## Still pending after homepage
Light **Flamingo** + **Roadrunner** PDPs (same `_imggen` pipeline / design system). Memory:
`project_proton_light_mode_rebrand`, `project_proton_canonical_messaging_v3`.
