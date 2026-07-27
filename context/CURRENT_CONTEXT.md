# Proton Peacock repo — CURRENT CONTEXT (2026-07-27)

## SESSION 2026-07-27: LOGO KIT + HERO ROTATION + PARTNERS (see context/NEXT_SESSION.json — SHIPPED, all pushed)
- Official wordmark on Peacock nav/footer; white-P atom (new kit file) on home navy band; dup wordmark deleted (5927237)
- Hero: random-per-visit rotation, action-first slices; a=Mike's 30s spot (audio kept), b=reel 2.375-12.79s, c=reel 17.92-28.42s; reel outro at 28.4s+ excluded (9ec46a4 -> 0a5f610)
- Partners: Paddle Battles Open replaces Hunter Games; Reset added (black->white knockout); grid 3x3 (0a5f610)
- REPO WAS ARCHIVED 2026-07-24; unarchived 2026-07-27 to push. Re-archive = Anthony's call.
- Live: https://tonyflo79.github.io/proton-peacock-pdp-preview/home.html

---

# PREVIOUS — CURRENT CONTEXT (2026-07-20)

## LIGHT-MODE CONVERSION: ROADRUNNER + FLAMINGO (this session — see context/NEXT_SESSION.json)
Peacock (`index.html`) + `home.html` were already light; Roadrunner + Flamingo PDPs were still DARK.
- **Roadrunner: DONE** — full CSS dark→light flip + all 5 gallery/feature images recolored & installed
  (dark backups in `roadrunner/assets/roadrunner/dark-backup/`). 05-build (dark neon-art) rebuilt as a
  clean light edgeless-frame shot (Anthony-approved).
- **Flamingo: CSS flip DONE, IMAGES PENDING** — recolor 8 pink images with `_imggen/recolor_v2.py --accent 214,53,126`, zoom-verify residue, back up darks.
- **NEW residue-free tool: `_imggen/recolor_v2.py`** (builds product silhouette, un-mattes edges over white).
- **Open both pages: nav+footer wordmark is white-on-white (invisible)** → swap to navy wordmark.
- `home.html`: built `assets/partners/proton-national-tour.png` + wired into 'Who we back'. Hunter Games = text placeholder (no logo yet).
- **Nothing committed. Branch feat/light-mode. Do NOT touch main.** HARD REQ: no black residue on paddle lettering/outline.

---

## (prior) HOMEPAGE v3 — REBUILT TO BRANT'S WIREFRAME (2026-07-15)

## HOMEPAGE v3 — REBUILT TO BRANT'S WIREFRAME (this session)
`home.html` was fully restructured from the v2 *editorial* page into the **hub layout**
Brant sketched (Downloads/IMG_5523.jpeg). Same approved light-mode PDP design system —
new information architecture. NOT committed, NOT pushed, NOT merged (merge is Anthony's).

**New module order (top → bottom):**
1. Promo bar — rotating announcements (Official Paddle of MLP / free shipping / new Roadrunner)
2. Search-forward nav — hamburger (slide-over drawer) · center search · Account/Cart
3. Brand header band — centered proton wordmark ("HEADER" in wireframe)
4. **Video hero** — `assets/hero/proton-hero.mp4` (muted autoplay loop, poster + sound toggle).
   Transcoded from `~/Downloads/PROTON.mov` (4K/38s → 1080p/13MB) via ffmpeg.
   Headline "Engineered like aerospace. Played on tour."
5. Trust strip — aerospace carbon / optimized spin / UPA + USA Pickleball certified
6. **3 equal category tiles** — Pickleball · Softball · Apparel (hover reveals sub-links = the
   wireframe "Desired Pop Up"). Softball gets equal billing = Brant's "10% more softball / less paddle-centric."
7. **What's New** — product scroller (Roadrunner NEW · Peacock · Flamingo · Softball bat)
8. **Instagram feed** — #protonsports grid (curated athlete/UGC + product). STATIC mock; see open items.
9. **Sponsorships (dark band)** — "The Official Paddle of MLP" + MLP logo slot + protonPROS roster
10. Footer — Pickleball / Softball / Company / Policies

## MIKE'S CERT CHANGE — APPLIED
- Old claim "Official Sponsor of the PPA + MLP" (and `assets/social/official-sponsor-ppa-mlp.png`
  tile) is GONE. New claim everywhere: **"Official Paddle of MLP"** (MLP only, PPA dropped).
- Kept SEPARATE and intact: **UPA + USA Pickleball** = equipment/tournament-legal cert (trust
  strip + footer). That is NOT the MLP sponsorship — do not merge the two.

## OPEN ITEMS (before final / for Anthony)
1. **MLP logo art** — the Sponsorships block uses a styled *placeholder* "MLP" slot (flagged in the
   UI + HTML comment near `.mlp-slot`). Drop in the official MLP logo (vector/PNG) before final.
   Anthony chose placeholder-for-now over cropping the old tile.
2. **Instagram feed is a static curated grid** — on the Shopify build, replace with a live IG-feed
   widget pulling #protonsports (Shopify IG app / EmbedSocial / Elfsight). HTML comment marks the spot.
3. `pablo-tellez.png` is a "SIGNED" announcement graphic (not a clean action headshot) — fine as an
   IG tile, slightly off as a roster portrait; swap if a clean Pablo photo turns up.
4. "Better Photos" note on the wireframe = Brant/team reminder to get better *product* photography.

## PROOFS
`~/Desktop/proton-HOMEPAGE-v3-wireframe-DESKTOP.png` (1440w) + `-MOBILE.png` (390w).
Old editorial homepage is preserved in git history (commit a2fa849:home.html).

## LIVE DEMO (updates only after push to feat/light-mode)
- Homepage: https://tonyflo79.github.io/proton-peacock-pdp-preview/home.html
- Peacock PDP (light): https://tonyflo79.github.io/proton-peacock-pdp-preview/
- Flamingo / Roadrunner PDPs (still DARK, bundled): /flamingo/ , /roadrunner/

## STILL-PENDING FROM BEFORE (unchanged)
Light Flamingo + Roadrunner PDP redos, then swap the `/flamingo` `/roadrunner` bundles so the
Pages demo goes all-light. Memory: `project_proton_light_mode_rebrand`, `project_proton_canonical_messaging_v3`.
