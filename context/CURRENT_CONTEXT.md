# Proton Peacock repo — CURRENT CONTEXT (2026-07-10)

## Just shipped (committed + pushed, branch `feat/light-mode`, commit 74a4156)
**Light homepage `home.html` v2** — built per HOMEPAGE-BUILD-HANDOFF.json, then reworked on
Anthony's corrections:
- **Hero:** H1 = "Pickleball, Engineered Like Aerospace." (grad on last two words); the previously
  locked line ("Aerospace-grade carbon fiber. Roughness-enhanced spin. With a high-performance
  core tuned to your game.") is now the SUBHEAD. CTAs + DNA strip unchanged.
- **Nav matches live site:** Pickleball · Softball · protonPROS · About Us · Warranty
  (anchors: #paddles / #beyond / #pros / #story / #faq).
- **Section order (Anthony-directed):** hero → #paddles (3 cards; Roadrunner now **$175**, live
  on protonsports.com) → **#pros protonPROS** (tour mosaic: jade-world1 broadcast still,
  official-sponsor PPA+MLP tile, Meghan Roadrunner cutout; + 3 five-star review cards lifted from
  Proton's Series-Four "Customer Reviews" creative — deliberately NOT the PDP pros grid) →
  **#beyond "One atom. Two sports."** (Softball bats from $170 / Apparel from $25 / Pickleball
  Backpack $65; images pulled from Shopify CDN into `assets/site/`; links to protonsports.com
  collections) → #technology AeroGrade → #story founder → cert band → #faq → close → footer
  (mirrors site menu: Pickleball/Softball/protonPROS/About·Warranty).
- Scrape facts (products.json): site sells softball bats ($170–$250, USSSA/USA-ASA/SSUSA-NSA-ISA),
  24 apparel SKUs ($25–$75), backpack $65, USA cap $30, "Any 2 Paddles $125 each" bundle exists,
  Roadrunner paddle live at $175.
- Desktop proof `proton-HOMEPAGE-lightmode-FULLPAGE.png` (1440×8453), self-reviewed at full res.
- NOT merged — merge is Anthony's. Awaiting his review of v2.

## NEXT (fresh session)
1. Anthony's feedback on homepage v2 (open questions: quiz still deferred; coming-soon treatment
   default used; Meghan tile caption is name-less — confirm if he wants her named).
2. Then: light **Flamingo** + **Roadrunner** PDPs (same `_imggen` pipeline / design system).

Memory: `project_proton_light_mode_rebrand`, `project_proton_canonical_messaging_v3`.
