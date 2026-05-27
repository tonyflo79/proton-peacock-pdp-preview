/* WF1 — Editorial Engineering · POLISHED LIGHT
   Final-ready wireframe with every image slot annotated with a concrete
   shot direction (role / shot / note). The Slot atom renders the shot
   list inside empty placeholders and floats an intent tag over filled
   product photography so the engineering team can see what should be
   in every slot at handoff time.
*/

const CP = window.COPY;
const { Slot: SlotP, Eyebrow: EyebrowP, Rule: RuleP, ChipGroup: ChipGroupP, PdpNav: PdpNavP, PdpFooter: PdpFooterP } = window.WF;

function WF1_Polished() {
  return (
    <div className="proton-wire" style={{ background: 'var(--p-ink)', color: 'var(--p-bone)', width: '100%' }}>
      <PdpNavP variant="editorial" />

      {/* — Breadcrumb — */}
      <div style={{ padding: '20px 64px', display:'flex', gap: 8, alignItems:'center' }}>
        <div className="p-micro" style={{ color:'var(--p-bone-3)' }}>Pickleball</div>
        <div className="p-micro" style={{ color:'var(--p-bone-4)' }}>/</div>
        <div className="p-micro" style={{ color:'var(--p-bone-3)' }}>Series Three</div>
        <div className="p-micro" style={{ color:'var(--p-bone-4)' }}>/</div>
        <div className="p-micro" style={{ color:'var(--p-teal)' }}>Project Peacock</div>
      </div>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S1 — ATF HERO */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ padding: '24px 64px 96px', background: 'var(--p-ink)' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '60fr 40fr', gap: 48 }}>
          {/* — Carousel left — */}
          <div>
            <SlotP
              src="assets/roughness.png"
              ratio="4/5"
              role="ATF · Slide 1"
              tag="Hero studio · branded face"
              style={{ marginBottom: 12 }}
            />
            <div style={{ display:'grid', gridTemplateColumns:'repeat(5, 1fr)', gap: 8 }}>
              <SlotP src="assets/roughness.png" ratio="1/1" tag="01" />
              <SlotP
                ratio="1/1"
                role="02"
                shot="Carbon weave macro"
                note="Raking key reveals the teal warp threads in the cured carbon. Frame fills with weave; no paddle silhouette."
              />
              <SlotP src="assets/atomic-core.png" ratio="1/1" tag="03 · core" />
              <SlotP
                ratio="1/1"
                role="04"
                shot="Dual-stamp detail"
                note="Macro of UPA-A and USAP stamps on paddle throat or back."
              />
              <SlotP src="assets/aeroweave.png" ratio="1/1" tag="05" />
            </div>
            <div className="p-micro" style={{ marginTop: 14, color: 'var(--p-bone-3)', fontSize: 11 }}>
              Slide 1 · {CP.s1.carousel[0]}
            </div>
          </div>

          {/* — Sticky buy-box right — */}
          <div style={{
            background: 'var(--p-ink-1)',
            border: '1px solid var(--p-hairline)',
            padding: 36,
            alignSelf:'start',
            position:'relative',
          }}>
            <div className="p-micro" style={{ position:'absolute', top:18, right:18, color:'var(--p-teal)' }}>
              Buy box · sticks to S10
            </div>
            <EyebrowP>{CP.s1.eyebrow}</EyebrowP>
            <h1 className="p-display" style={{
              fontSize: 44, fontWeight: 400, marginTop: 18, marginBottom: 20, letterSpacing:'-0.03em',
            }}>{CP.s1.headline}</h1>
            <p className="p-body" style={{ fontSize: 17, marginBottom: 28, color: 'var(--p-bone-2)' }}>
              {CP.s1.deck}
            </p>

            <div style={{ display:'flex', alignItems:'baseline', gap: 16, marginBottom: 8 }}>
              <div style={{ fontFamily:'var(--ff-display)', fontWeight: 500, fontSize: 34, letterSpacing:'-0.02em' }}>
                {CP.s1.priceLong} <span style={{ fontFamily:'var(--ff-mono)', fontSize: 12, color:'var(--p-bone-3)', letterSpacing:'0.12em', marginLeft: 4 }}>ELONGATED</span>
              </div>
            </div>
            <div style={{ display:'flex', alignItems:'baseline', gap: 16, marginBottom: 8 }}>
              <div style={{ fontFamily:'var(--ff-display)', fontWeight: 500, fontSize: 34, letterSpacing:'-0.02em' }}>
                {CP.s1.priceWide} <span style={{ fontFamily:'var(--ff-mono)', fontSize: 12, color:'var(--p-bone-3)', letterSpacing:'0.12em', marginLeft: 4 }}>WIDE-BODY</span>
              </div>
            </div>
            <div style={{ marginBottom: 28, fontFamily:'var(--ff-mono)', fontSize: 12, color:'var(--p-bone-4)' }}>
              Was <span style={{ textDecoration: 'line-through' }}>{CP.s1.priceWas}</span> · launch pricing below
            </div>

            <RuleP style={{ marginBottom: 24 }} />

            <div style={{ display:'flex', flexDirection:'column', gap: 18, marginBottom: 28 }}>
              <ChipGroupP label="Shape" options={['Elongated','Wide-Body']} selected={0} />
              <ChipGroupP label="Thickness" options={['13mm','15mm']} selected={0} />
            </div>

            <button className="p-btn" style={{ width:'100%', marginBottom: 16 }}>
              {CP.s1.cta} <span style={{ marginLeft: 4 }}>→</span>
            </button>
            <div className="p-body" style={{ fontSize: 13, textAlign:'center', color:'var(--p-bone-3)', marginBottom: 28 }}>
              {CP.s1.microTrust}
            </div>

            <RuleP style={{ marginBottom: 24 }} />

            <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap: 10 }}>
              {CP.s1.badges.map((b, i) => (
                <div key={i} style={{
                  border: '1px solid var(--p-hairline-3)', padding: '12px 12px', borderRadius: 2,
                  fontFamily: 'var(--ff-mono)', fontSize: 10.5, letterSpacing: '0.08em',
                  textTransform: 'uppercase', color: 'var(--p-bone-2)', lineHeight: 1.35,
                }}>{b}</div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S2 — OPEN */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-1)', padding: '112px 64px', textAlign:'center' }}>
        <div className="p-micro" style={{ color:'var(--p-bone-4)', marginBottom: 24 }}>02 · PROMISE</div>
        <p className="p-display" style={{
          fontSize: 36, fontWeight: 300, lineHeight: 1.35, maxWidth: 880, margin: '0 auto',
          color: 'var(--p-bone)', letterSpacing: '-0.02em',
        }}>{CP.s2}</p>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S3 — REFRAME */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 880, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 20 }}>03 · Construction</EyebrowP>
          <p className="p-body" style={{ fontSize: 19, lineHeight: 1.6, color:'var(--p-bone)' }}>
            {CP.s3.body}
          </p>
          <hr className="p-rule-teal" style={{ margin: '48px auto', width: 64, marginLeft: 0 }} />
          <p style={{ fontFamily: 'var(--ff-display)', fontSize: 48, fontWeight: 300, letterSpacing:'-0.03em', lineHeight: 1.05 }}>
            <span className="p-gradient-text">{CP.s3.pullquote}</span>
          </p>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S4 — AeroWeave Mechanism */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-2)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 16 }}>04 · Mechanism</EyebrowP>
          <h2 className="p-display" style={{ fontSize: 56, marginBottom: 32, fontWeight: 400 }}>
            <span className="p-gradient-text">{CP.s4.headline}</span>
          </h2>
          <p className="p-body" style={{ fontSize: 17, lineHeight: 1.65, maxWidth: 820, color:'var(--p-bone-2)', marginBottom: 80 }}>
            {CP.s4.lede}
          </p>

          <div style={{ display:'flex', flexDirection:'column', gap: 72 }}>
            {[
              {
                src: 'assets/aeroweave.png',
                role: 'Step 01',
                tag: 'Carbon fiber face',
                shot: 'Full paddle, raking light across the face',
                note: 'Single hero paddle, slight 3/4 angle. Strong directional key reveals the texture of the aerospace grade carbon fiber face.',
              },
              {
                src: 'assets/roughness.png',
                role: 'Step 02',
                tag: 'Weave macro · teal warp',
                shot: 'Macro of carbon weave',
                note: 'Inset crop matches the inline image; fills 70% of frame. Teal threads catch raking light. No paddle silhouette.',
              },
              {
                src: 'assets/atomic-core.png',
                role: 'Step 03',
                tag: 'Atomic core cutaway',
                shot: 'Side view, core visible',
                note: 'Edge-on view of the paddle revealing the dense atomic foam core through a section cut or transparency overlay.',
              },
              {
                role: 'Step 04',
                shot: 'Dual-stamp certification',
                note: 'Macro of UPA-A + USAP stamps on the paddle throat. Both stamps in frame, sharp focus. Subtle ambient light.',
              },
              {
                role: 'Step 05',
                shot: 'Warranty / signature detail',
                note: 'Care booklet flat-lay with paddle handle and serial number tag. Stone or matte black surface. Single soft key from upper-left.',
              },
            ].map((s, i) => {
              const left = i % 2 === 0;
              return (
                <div key={i} style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap: 56, alignItems:'center' }}>
                  <div style={{ order: left ? 1 : 2 }}>
                    <SlotP src={s.src} role={s.role} tag={s.tag} shot={s.shot} note={s.note} ratio="4/3" />
                  </div>
                  <div style={{ order: left ? 2 : 1 }}>
                    <div className="p-num" style={{ fontSize: 88, color:'var(--p-bone-3)', marginBottom: 14, fontWeight: 200 }}>
                      {String(i+1).padStart(2, '0')}
                    </div>
                    <div className="p-micro" style={{ color:'var(--p-teal)', marginBottom: 16 }}>
                      {CP.s4.stepHeaders[i].split('· ')[1]}
                    </div>
                    <p className="p-body" style={{ fontSize: 17, lineHeight: 1.6, color:'var(--p-bone-2)' }}>{CP.s4.steps[i]}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S5 — Feature grid + Founder */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-1)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 1200, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 16 }}>05 · The build</EyebrowP>
          <h2 className="p-display" style={{ fontSize: 56, fontWeight: 400, marginBottom: 64 }}>{CP.s5.heading}</h2>

          {(() => {
            const tileShots = [
              { src: 'assets/atomic-core.png', role: 'Tile 01', tag: 'Atomic core · cutaway' },
              { src: 'assets/aeroweave.png',   role: 'Tile 02', tag: 'AeroWeave · paddle hero' },
              { src: 'assets/roughness.png',   role: 'Tile 03', tag: 'Weave · teal warp macro' },
              { role: 'Tile 04', shot: 'Aerospace grade carbon fiber face', note: 'Paddle face filling the frame, light gradient reveals the carbon weave texture. Studio set; no environment.' },
              { role: 'Tile 05', shot: 'Dual-stamped approval', note: 'Both UPA-A and USAP stamps in single macro frame. Centered, sharp focus, dark glass.' },
              { role: 'Tile 06', shot: 'Lifetime warranty', note: 'Care booklet + paddle handle flat-lay. Stone or warm bone surface. Single soft key.' },
            ];
            return (
              <div style={{ display:'grid', gridTemplateColumns:'repeat(3, 1fr)', gap: 20 }}>
                {CP.s5.tiles.map((t, i) => {
                  const s = tileShots[i];
                  return (
                    <div key={i} style={{
                      background: 'var(--p-ink-2)',
                      border: t.hero ? '1px solid var(--p-teal)' : '1px solid var(--p-hairline)',
                      padding: 24, position: 'relative', minHeight: 380,
                    }}>
                      {t.hero && (
                        <div style={{
                          position:'absolute', top:16, right:16,
                          fontFamily:'var(--ff-mono)', fontSize: 10, color:'var(--p-teal)',
                          letterSpacing:'0.2em', textTransform:'uppercase',
                        }}>● HERO</div>
                      )}
                      <SlotP
                        ratio="1/1"
                        style={{ marginBottom: 20 }}
                        src={s.src}
                        role={s.role}
                        tag={s.tag}
                        shot={s.shot}
                        note={s.note}
                      />
                      <div className="p-micro" style={{ color:'var(--p-bone-4)', marginBottom: 6 }}>{String(i+1).padStart(2,'0')}</div>
                      <h3 style={{ fontFamily:'var(--ff-display)', fontSize: 20, fontWeight: 500, lineHeight: 1.2, marginBottom: 10, letterSpacing:'-0.01em' }}>{t.name}</h3>
                      <p className="p-body" style={{ fontSize: 14, lineHeight: 1.55, color:'var(--p-bone-2)' }}>{t.body}</p>
                    </div>
                  );
                })}
              </div>
            );
          })()}

          <div style={{ display:'flex', justifyContent:'center', marginTop: 64 }}>
            <button className="p-btn">{CP.s5.inlineCta} <span>→</span></button>
          </div>

          {/* Founder block */}
          <RuleP style={{ margin: '96px 0 64px' }} />
          <div style={{ display:'grid', gridTemplateColumns:'300px 1fr', gap: 56, alignItems:'start' }}>
            <div>
              <SlotP
                ratio="1/1"
                role="Founder portrait"
                shot="Environmental portrait · Charles Darling"
                note="Composite-cure oven, layup table, or autoclave environment. Workwear or lab coat. Three-quarter angle, eyes off-camera, no smile. Warm key + cool fill. Avoid stage-marketing pose."
              />
              <div className="p-micro" style={{ marginTop: 14, color:'var(--p-bone-3)' }}>{CP.s5.founderCaption}</div>
            </div>
            <div>
              <EyebrowP style={{ marginBottom: 18 }}>The engineer behind the build</EyebrowP>
              <p className="p-body" style={{ fontSize: 18, lineHeight: 1.6, color:'var(--p-bone)' }}>{CP.s5.founder}</p>
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S6 — Counter */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink)', padding: '128px 64px', textAlign:'center' }}>
        <EyebrowP style={{ marginBottom: 32, color:'var(--p-bone-4)' }}>06</EyebrowP>
        <p className="p-display" style={{
          fontSize: 32, fontWeight: 300, lineHeight: 1.45,
          maxWidth: 880, margin: '0 auto', letterSpacing:'-0.015em', color: 'var(--p-bone)',
        }}>{CP.s6}</p>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S7 — Proof */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-1)', padding: '128px 64px', textAlign:'center' }}>
        <div style={{ maxWidth: 1000, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 32 }}>07 · Proof</EyebrowP>

          <div style={{ display:'grid', gridTemplateColumns:'repeat(4, 1fr)', gap: 16, marginBottom: 56 }}>
            {CP.s7.badges.map((b, i) => {
              const shotNotes = [
                'Real UPA-A stamp graphic (pending from Proton ops)',
                'Real USAP stamp graphic (pending from Proton ops)',
                'Lifetime Warranty seal — custom Proton mark',
                '30-Day Money-Back seal — custom Proton mark',
              ];
              return (
                <div key={i} className="p-badge" style={{ position:'relative' }}>
                  <div style={{ width: 56, height: 56, borderRadius: '50%', border: '1px solid var(--p-teal)', display:'flex', alignItems:'center', justifyContent:'center', marginBottom: 14 }}>
                    <span className="p-gradient-text" style={{ fontFamily:'var(--ff-display)', fontWeight: 500, fontSize: 14 }}>{['UPA','USAP','∞','30d'][i]}</span>
                  </div>
                  <div className="p-badge-body">{b}</div>
                  <div style={{
                    fontFamily:'var(--ff-mono)', fontSize: 9, color:'var(--p-bone-4)',
                    letterSpacing:'0.1em', marginTop: 10, textTransform:'uppercase',
                  }}>BADGE · {shotNotes[i].split(' ')[0]}</div>
                </div>
              );
            })}
          </div>

          <p className="p-body" style={{ fontSize: 17, lineHeight: 1.65, color:'var(--p-bone-2)', maxWidth: 820, margin: '0 auto 48px' }}>{CP.s7.body}</p>
          <RuleP teal style={{ width: 64, margin: '0 auto 32px' }} />
          <p className="p-display" style={{ fontSize: 32, fontWeight: 400, letterSpacing:'-0.02em' }}>
            <span className="p-gradient-text">{CP.s7.pullquote}</span>
          </p>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S8 — SKU Selector */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 16 }}>08 · Configure</EyebrowP>
          <h2 className="p-display" style={{ fontSize: 56, fontWeight: 400, marginBottom: 14 }}>{CP.s8.heading}</h2>
          <p className="p-body" style={{ fontSize: 17, color:'var(--p-bone-3)', marginBottom: 56 }}>{CP.s8.helper}</p>

          <div className="p-micro" style={{ color:'var(--p-teal)', marginBottom: 20 }}>Shape</div>
          <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap: 20, marginBottom: 48 }}>
            {CP.s8.shapes.map((s, i) => (
              <div key={i} style={{
                background: 'var(--p-ink-2)',
                border: i === 0 ? '1px solid var(--p-teal)' : '1px solid var(--p-hairline)',
                padding: 24, display:'grid', gridTemplateColumns:'180px 1fr', gap: 24,
              }}>
                <SlotP
                  ratio="2/3"
                  role={`Shape ${i+1}`}
                  shot={`${s.name.split(' ')[0]} silhouette`}
                  note="Clean flat-vector silhouette. Black-on-bone, accurate proportions, no shading. Technical-drawing style."
                />
                <div>
                  <div style={{ display:'flex', justifyContent:'space-between', alignItems:'baseline', marginBottom: 10 }}>
                    <h3 style={{ fontFamily:'var(--ff-display)', fontSize: 22, fontWeight: 500, letterSpacing:'-0.01em' }}>{s.name}</h3>
                    <div style={{ fontFamily:'var(--ff-display)', fontSize: 22, fontWeight: 500 }}>{s.price}</div>
                  </div>
                  <p className="p-body" style={{ fontSize: 14, lineHeight: 1.5, color:'var(--p-bone-2)' }}>{s.body}</p>
                  <div style={{ marginTop: 14, display:'flex', alignItems:'center', gap: 8 }}>
                    <div style={{
                      width: 14, height: 14, borderRadius: '50%',
                      border: i === 0 ? '4px solid var(--p-teal)' : '1px solid var(--p-bone-4)',
                    }} />
                    <div className="p-micro" style={{ color: i === 0 ? 'var(--p-teal)' : 'var(--p-bone-4)' }}>
                      {i === 0 ? 'Selected' : 'Select'}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="p-micro" style={{ color:'var(--p-teal)', marginBottom: 20 }}>Thickness</div>
          <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap: 20, marginBottom: 64 }}>
            {CP.s8.thickness.map((t, i) => (
              <div key={i} style={{
                background: 'var(--p-ink-2)',
                border: i === 0 ? '1px solid var(--p-teal)' : '1px solid var(--p-hairline)',
                padding: 24,
              }}>
                <SlotP
                  ratio="16/9"
                  role={`Thickness ${i+1}`}
                  shot={`Cross-section · ${t.name.split(' ')[0]}`}
                  note="Schematic vector showing carbon face / atomic foam core / carbon back. Layer labels in mono. Teal accent on the core layer."
                  style={{ marginBottom: 18 }}
                />
                <h3 style={{ fontFamily:'var(--ff-display)', fontSize: 20, fontWeight: 500, marginBottom: 8, letterSpacing:'-0.01em' }}>{t.name}</h3>
                <p className="p-body" style={{ fontSize: 14, lineHeight: 1.5, color:'var(--p-bone-2)' }}>{t.body}</p>
              </div>
            ))}
          </div>

          <button className="p-btn" style={{ width:'100%' }}>
            {CP.s8.cta} · $195 · Elongated · 13mm <span>→</span>
          </button>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S9 — Promise Land */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-2)', padding: '160px 64px', textAlign:'center' }}>
        <EyebrowP style={{ marginBottom: 40 }}>09 · The promise</EyebrowP>
        <h2 className="p-display" style={{
          fontSize: 64, fontWeight: 300, lineHeight: 1.18, maxWidth: 1000, margin: '0 auto', letterSpacing:'-0.03em',
        }}>
          <span className="p-gradient-text">{CP.s9}</span>
        </h2>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S10 — Offer */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 1100, margin: '0 auto' }}>
          <div style={{ display:'grid', gridTemplateColumns:'1fr 1fr', gap: 64, alignItems:'center', marginBottom: 56 }}>
            <SlotP src="assets/roughness.png" ratio="4/5" role="Offer hero" tag="Branded face · Elongated 13mm" />
            <div>
              <EyebrowP style={{ marginBottom: 20 }}>10 · The offer</EyebrowP>
              <h2 className="p-display" style={{ fontSize: 56, fontWeight: 400, marginBottom: 16, letterSpacing:'-0.025em' }}>{CP.s10.name}</h2>
              <div className="p-body" style={{ fontSize: 18, color:'var(--p-bone-2)', marginBottom: 32, fontFamily:'var(--ff-mono)', letterSpacing: '0.04em' }}>{CP.s10.price}</div>
              <p className="p-body" style={{ fontSize: 15, lineHeight: 1.65, color:'var(--p-bone-2)' }}>{CP.s10.body}</p>
            </div>
          </div>

          <div style={{ display:'grid', gridTemplateColumns:'repeat(5, 1fr)', gap: 14, marginBottom: 40 }}>
            {CP.s10.icons.map((ic, i) => (
              <div key={i} style={{
                display:'flex', flexDirection:'column', alignItems:'center', gap: 10,
                padding: 16, border: '1px solid var(--p-hairline)', borderRadius: 2,
              }}>
                <div style={{ width: 36, height: 36, borderRadius: '50%', border: '1px solid var(--p-teal)' }} />
                <div className="p-micro" style={{ fontSize: 10, color:'var(--p-bone-2)', textAlign:'center', lineHeight: 1.3 }}>{ic}</div>
              </div>
            ))}
          </div>

          <button className="p-btn" style={{ width:'100%', height: 64, fontSize: 16 }}>{CP.s10.cta} <span>→</span></button>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S11 — FAQ */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-1)', padding: '128px 64px' }}>
        <div style={{ maxWidth: 880, margin: '0 auto' }}>
          <EyebrowP style={{ marginBottom: 16 }}>11 · FAQ</EyebrowP>
          <h2 className="p-display" style={{ fontSize: 48, fontWeight: 400, marginBottom: 56 }}>{CP.s11.heading}</h2>

          <div style={{ display:'flex', flexDirection:'column' }}>
            {CP.s11.items.map((it, i) => (
              <div key={i} style={{
                borderTop: '1px solid var(--p-hairline)',
                padding: '24px 0',
                ...(i === CP.s11.items.length - 1 ? { borderBottom: '1px solid var(--p-hairline)' } : {}),
              }}>
                <div style={{ display:'flex', alignItems:'flex-start', gap: 16 }}>
                  <div className="p-micro" style={{ color:'var(--p-bone-4)', minWidth: 32, paddingTop: 4 }}>{String(i+1).padStart(2,'0')}</div>
                  <div style={{ flex: 1 }}>
                    <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between' }}>
                      <h3 style={{ fontFamily:'var(--ff-display)', fontSize: 19, fontWeight: 500, lineHeight: 1.3, letterSpacing:'-0.01em' }}>
                        {it.q}
                        {it.emph && <span className="p-micro" style={{ marginLeft: 14, color:'var(--p-teal)' }}>Most asked</span>}
                      </h3>
                      <div style={{ color:'var(--p-bone-3)', fontSize: 20, marginLeft: 16 }}>{it.emph ? '−' : '+'}</div>
                    </div>
                    {it.emph && (
                      <p className="p-body" style={{ fontSize: 15, lineHeight: 1.6, color:'var(--p-bone-2)', marginTop: 16 }}>{it.a}</p>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════════════ */}
      {/* S12 — Close */}
      {/* ═══════════════════════════════════════════════════════════ */}
      <section style={{ background: 'var(--p-ink-2)', padding: '160px 64px 128px', textAlign:'center' }}>
        <EyebrowP style={{ marginBottom: 40 }}>12 · The Atomic Core paddle</EyebrowP>
        <h2 className="p-display" style={{
          fontSize: 64, fontWeight: 300, lineHeight: 1.15, maxWidth: 920, margin: '0 auto 56px', letterSpacing:'-0.03em',
        }}>
          <span className="p-gradient-text">{CP.s12.anchor}</span>
        </h2>
        <button className="p-btn" style={{ height: 64, fontSize: 16, padding: '0 40px' }}>{CP.s12.cta} <span>→</span></button>
        <div className="p-body" style={{ fontSize: 13, color:'var(--p-bone-3)', marginTop: 24 }}>{CP.s12.microTrust}</div>
      </section>

      <PdpFooterP />
    </div>
  );
}

window.WF1_Polished = WF1_Polished;
