/* Shared atoms for all 3 Proton PDP wireframes */

const Slot = ({ label, desc, ratio = '4/5', style, children, src, shot, note, tag, role }) => (
  <div className="p-slot" style={{ aspectRatio: ratio, ...style }}>
    {src ? (
      <>
        <img src={src} alt={label || shot || ''} style={{ position:'absolute', inset:0, width:'100%', height:'100%', objectFit:'cover', objectPosition:'center' }} />
        {(tag || role) && (
          <div className="p-slot-tag-overlay">
            {role && <span className="p-slot-role">{role}</span>}
            {tag && <span className="p-slot-tag-text">{tag}</span>}
          </div>
        )}
      </>
    ) : (
      <div className="p-slot-shotlist">
        {role && <div className="p-slot-role">{role}</div>}
        {(shot || label) && <div className="p-slot-shot">{shot || label}</div>}
        {(note || desc) && <div className="p-slot-note">{note || desc}</div>}
        {children}
      </div>
    )}
  </div>
);

const Eyebrow = ({ children, style }) => (
  <div className="p-eyebrow" style={style}>{children}</div>
);

const Rule = ({ teal, style }) => (
  <hr className={teal ? 'p-rule-teal' : 'p-rule'} style={style} />
);

// Variant chip selector group
const ChipGroup = ({ label, options, selected, onSelect }) => (
  <div style={{ display:'flex', flexDirection:'column', gap:8 }}>
    <div className="p-micro" style={{ color:'var(--p-bone-3)' }}>{label}</div>
    <div style={{ display:'flex', gap:8 }}>
      {options.map((o, i) => (
        <div key={i} className={'p-chip' + (selected === i ? ' p-chip-on' : '')}>
          {o}
        </div>
      ))}
    </div>
  </div>
);

// Page-level nav (sticky-ish at top of each wireframe artboard)
const PdpNav = ({ variant = 'editorial' }) => (
  <div style={{
    height: 64,
    borderBottom: '1px solid var(--p-hairline)',
    display: 'flex',
    alignItems: 'center',
    padding: '0 32px',
    background: 'var(--p-nav-bg)',
    backdropFilter: 'blur(8px)',
    position: 'relative',
    zIndex: 5,
  }}>
    {/* Proton P mark — simple gradient circle with atom motif */}
    <div style={{ display:'flex', alignItems:'center', gap:10 }}>
      <div style={{
        width: 28, height: 28, borderRadius: '50%',
        background: 'var(--p-peacock)',
        display:'flex', alignItems:'center', justifyContent:'center',
        fontFamily: 'var(--ff-display)', fontWeight: 600, fontSize: 14, color: '#07070A',
      }}>p</div>
      <div style={{ fontFamily:'var(--ff-display)', fontWeight: 500, letterSpacing: '0.16em', fontSize: 13, textTransform:'uppercase' }}>PROTON</div>
    </div>
    <div style={{ display:'flex', gap:28, marginLeft: 56 }}>
      {['Pickleball','Series Three','Tour','Story','Support'].map(l => (
        <div key={l} className="p-micro" style={{ color:'var(--p-bone-2)', fontSize: 11 }}>{l}</div>
      ))}
    </div>
    <div style={{ marginLeft:'auto', display:'flex', alignItems:'center', gap:18 }}>
      <div className="p-micro" style={{ color:'var(--p-bone-3)' }}>Search</div>
      <div className="p-micro" style={{ color:'var(--p-bone-3)' }}>Account</div>
      <div className="p-micro" style={{ color:'var(--p-teal)' }}>Cart · 0</div>
    </div>
  </div>
);

// Footer (kept minimal — wireframe-level only)
const PdpFooter = ({ variant }) => (
  <div style={{
    background: 'var(--p-ink-1)',
    borderTop: '1px solid var(--p-hairline-2)',
    padding: '64px 64px 48px',
    color: 'var(--p-bone-3)',
  }}>
    <div style={{ display:'grid', gridTemplateColumns: '2fr 1fr 1fr 1fr 1fr', gap: 48, marginBottom: 48 }}>
      <div>
        <div style={{ fontFamily:'var(--ff-display)', fontSize: 22, fontWeight: 500, color:'var(--p-bone)', letterSpacing:'-0.02em', marginBottom: 12 }}>
          Powered by Protons.
        </div>
        <div className="p-body" style={{ fontSize: 13, maxWidth: 360, color:'var(--p-bone-3)' }}>
          Proton Sports — engineered pickleball paddles, designed by aerospace engineers in the United States.
        </div>
      </div>
      {[
        { h: 'Shop', items: ['Series Three','Tour Bag','Grips','Care kit'] },
        { h: 'Story', items: ['Engineering','Charles Darling','Proton Tour'] },
        { h: 'Support', items: ['Warranty','Shipping','Returns','Contact'] },
        { h: 'Legal', items: ['Terms','Privacy','Accessibility'] },
      ].map(col => (
        <div key={col.h}>
          <div className="p-micro" style={{ color:'var(--p-teal)', marginBottom: 14 }}>{col.h}</div>
          {col.items.map(i => <div key={i} className="p-body" style={{ fontSize: 13, marginBottom: 6 }}>{i}</div>)}
        </div>
      ))}
    </div>
    <hr className="p-rule" />
    <div style={{ display:'flex', justifyContent:'space-between', marginTop: 24 }}>
      <div className="p-micro">© 2026 Proton Sports · Engineered in the United States</div>
      <div className="p-micro">Dual-stamp UPA-A + USAP · Lifetime warranty on construction</div>
    </div>
  </div>
);

window.WF = { Slot, Eyebrow, Rule, ChipGroup, PdpNav, PdpFooter };
