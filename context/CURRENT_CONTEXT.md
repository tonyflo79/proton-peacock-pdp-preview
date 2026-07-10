# Proton Peacock repo — CURRENT CONTEXT (2026-07-10)

## LIVE CLIENT DEMO — GitHub Pages (branch `feat/light-mode`, legacy build on every push)
- **Homepage:** https://tonyflo79.github.io/proton-peacock-pdp-preview/home.html
- **Peacock PDP (light):** https://tonyflo79.github.io/proton-peacock-pdp-preview/
- **Flamingo PDP (dark, bundled):** https://tonyflo79.github.io/proton-peacock-pdp-preview/flamingo/
- **Roadrunner PDP (dark, bundled):** https://tonyflo79.github.io/proton-peacock-pdp-preview/roadrunner/

Pages source = `feat/light-mode` / root. Flamingo + Roadrunner PDPs were **copied** from their
sibling repos (`~/code/proton-{flamingo,roadrunner}-pdp-preview`) into `/flamingo` and
`/roadrunner` (commit 02a8ec2) — those copies are SNAPSHOTS; if the sibling repos change,
re-copy. Homepage paddle cards now link through to all 3 PDPs (coming-soon chips removed —
both paddles are live at $175 on protonsports.com). NOTE: Flamingo/Roadrunner are still DARK
mode behind a light homepage — light redos are the next build; swap the bundles in place when done.

## Homepage v2 state (commit 74a4156 + 02a8ec2)
- Hero H1 "Pickleball, Engineered Like Aerospace." (grad on last two words); old locked line is
  the subhead. Nav + footer mirror protonsports.com (Pickleball · Softball · protonPROS ·
  About Us · Warranty).
- Order: hero → #paddles (Peacock/Flamingo/Roadrunner, all linked, $175) → #pros protonPROS
  (tour mosaic: jade-world1, official PPA+MLP sponsor tile, Meghan Roadrunner cutout; 3 five-star
  review cards from Proton's Series-Four creative) → #beyond "One atom. Two sports." (bats from
  $170 / apparel from $25 / backpack $65, images in `assets/site/`, links to live collections) →
  #technology AeroGrade → #story founder → cert band → #faq → close → footer.
- Desktop proof `proton-HOMEPAGE-lightmode-FULLPAGE.png`. NOT merged — merge is Anthony's.

## Open questions for Anthony
- Name the Roadrunner action-shot player? (file says "Meghan"; caption currently name-less)
- 5-Q find-your-paddle quiz still deferred to v2.
- Dark Flamingo/Roadrunner behind light homepage OK for the demo, or hold links until light redos?

## NEXT (fresh session)
Light **Flamingo** + **RoadRunner** PDP redos (same `_imggen` pipeline / design system as Peacock),
then replace the `/flamingo` and `/roadrunner` bundles in this repo so the Pages demo goes
all-light. Memory: `project_proton_light_mode_rebrand`, `project_proton_canonical_messaging_v3`.
