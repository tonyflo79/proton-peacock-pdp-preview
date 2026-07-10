# Proton Peacock light-mode — HANDOFF (2026-07-10, mid-fix)

## VERDICT — STOP using recolor.py. Rebuild ALL 9 images via HTML.
Recoloring the flattened dark composites FAILED. Confirmed defects Anthony caught:
- **03 carbon loupe = erased empty** (dark-pixel cleanup wiped the photographic carbon-weave zoom).
- **01 paddle = black notch on top-left edge** (black-bg flood-fill leaked INTO the dark paddle face).
- Text/counter whack-a-mole.
Root cause: flood-fill fights the paddle's own near-black pixels and destroys exterior photographic insets. Unfixable cleanly.
**Do NOT recolor.** Rebuild every image in the HTML→Chrome pipeline using TRANSPARENT renders = perfect edges by construction, crisp native text, real leader lines, cropped photographic zooms. This is already proven clean on 05/08/09 and the first 01.

## Pipeline (in `_imggen/`)
`base.css` (light system: .stage, .paddle, .leads SVG, .lab, .loupe/.loupe-ring, .seal, .title) + one `NN.html` per image + `render.sh <html> <out>` (headless Chrome, 2048²). Transparent source renders in `_imggen/src/`. Dark originals in `_imggen/dark-backup/`.

## DONE + CLEAN (HTML): 01-aerograde, 05-warranty, 08-13mm, 09-15mm
- 01 uses `src/E-15mm-005.png` (straight front) + 5 leader callouts. GOOD — reinstall this HTML version (currently assets/ has the bad recolored 01).

## STILL TO BUILD as HTML: 02, 03, 04, 06, 07
Exact layout + text (match originals, "identical except color"):
- **02 foam-core**: split cutaway paddle. LEFT half = core interior (`src/core.png` = Peacock-Core.png 1080x1350), RIGHT half = real paddle face. 4 left callouts: FOAM-INJECTED EDGE GUARD / ELASTIC EVA FOAM PERIMETER / HIGH-DENSITY ATOMIC FOAM CORE / FOAM THROUGH THE HANDLE. Title: HIGH-DENSITY ATOMIC FOAM CORE — sub: DENSE. CONSISTENT. BUILT FOR EXTRA DURABILITY.
- **03 carbon-face**: paddle upper-LEFT + small square marker on face + connector line to BIG rounded-square loupe on RIGHT showing carbon twill weave. Title: AEROSPACE GRADE CARBON FIBER FACE — sub: ROUGHNESS ENHANCED. OPTIMIZED SPIN. → crop the weave from `dark-backup/03-carbon-face.png` (right loupe region ~x1400-1950,y780-1250) as a clean square asset.
- **04 dual-stamp**: paddle + connector to loupe showing the UPA/USA throat stamp macro. Title: DUAL-STAMPED APPROVAL — sub: PUSHING THE LEGAL MAXIMUM OF PERFORMANCE. → crop stamp from `dark-backup/04-dual-stamp.png` loupe region.
- **06 elongated**: straight Elongated render (`src/E-13mm-003` or E-15mm-005) + title ELONGATED — sub: MORE REACH. MORE SPEED. EXTRA SPIN LEVERAGE.
- **07 wide-body**: straight Square render (`src/S-15mm-003` or S-13mm-006) + title WIDE BODY — sub: BIGGER SWEET SPOT. MAXIMUM FORGIVENESS.

## After building all 9
1. `bash render.sh NN.html out/NN-light.png` for each.
2. Assemble a contact sheet and **self-review at FULL detail — catch every edge artifact / missing element / distortion YOURSELF. Anthony must not be the QA.**
3. Install to `assets/peacock/NN.png`, `open index.html`, verify in-page.

## State
- Repo `~/code/proton-peacock-pdp-preview`, branch `feat/light-mode` (NOT committed; merge is Anthony's).
- `index.html` CSS already flipped dark→light (good, keep).
- Then: roll to Flamingo + Roadrunner (photos in `~/Downloads/2025_10 Proton Paddle Photos/`), then net-new light HOMEPAGE = fresh conversion hero.
- Memory: `project_proton_light_mode_rebrand`.
