// LA REAL — Apply Modal (mini-selector + 2 forms + calendar booking)
// Exposes: window.D3Apply = { Modal, openSelector(), openForm(type) }
// `type` is 'partner' | 'advisor'.

(() => {
  const { useState, useEffect, useMemo, useCallback, useRef } = React;

  // ------- Global open/close bridge -------
  // d3.jsx wires CTAs via window.D3Apply.openSelector() / openForm('partner'|'advisor')
  let setOpenState = null;

  function openSelector() {
    setOpenState && setOpenState({ open: true, step: 'selector', type: null });
  }
  function openForm(type) {
    if (type !== 'partner' && type !== 'advisor') type = 'partner';
    setOpenState && setOpenState({ open: true, step: 'form', type });
  }
  function close() {
    setOpenState && setOpenState({ open: false, step: 'selector', type: null });
  }

  // ------- Helpers -------
  function isWeekend(d) { const w = d.getDay(); return w === 0 || w === 6; }
  function fmtDateISO(d) {
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }
  function fmtDateLabel(d, lang) {
    return d.toLocaleDateString(lang === 'es' ? 'es-CO' : 'en-US', {
      weekday: 'long', day: 'numeric', month: 'long',
    });
  }
  function fmtTimeLabel(time, lang) {
    // "14:00" -> "2:00 PM" (en) or "2:00 p. m." (es)
    const [h, m] = time.split(':').map(Number);
    const d = new Date(); d.setHours(h, m, 0, 0);
    return d.toLocaleTimeString(lang === 'es' ? 'es-CO' : 'en-US', {
      hour: 'numeric', minute: '2-digit', hour12: true,
    });
  }
  function monthLabel(d, lang) {
    return d.toLocaleDateString(lang === 'es' ? 'es-CO' : 'en-US', {
      month: 'long', year: 'numeric',
    });
  }
  function startOfMonth(d) { return new Date(d.getFullYear(), d.getMonth(), 1); }
  function addMonths(d, n) { return new Date(d.getFullYear(), d.getMonth() + n, 1); }

  // Build the grid of days for the visible month, padded so it always starts Monday
  function buildMonthGrid(monthStart) {
    const firstDow = monthStart.getDay(); // 0 = Sun
    const offset = (firstDow + 6) % 7; // shift so Monday = 0
    const start = new Date(monthStart);
    start.setDate(start.getDate() - offset);
    const days = [];
    for (let i = 0; i < 42; i++) {
      const d = new Date(start);
      d.setDate(start.getDate() + i);
      days.push(d);
    }
    return days;
  }

  // ------- Styles (scoped via .lr-apply prefix) -------
  const STYLES = `
    .lr-apply-overlay { position:fixed; inset:0; z-index:1000; display:flex; align-items:center; justify-content:center;
      background:rgba(6,8,12,.72); backdrop-filter:blur(8px); padding:24px; animation:lrFade .18s ease-out; }
    @keyframes lrFade { from { opacity:0 } to { opacity:1 } }
    @keyframes lrSlide { from { opacity:0; transform:translateY(12px) } to { opacity:1; transform:translateY(0) } }

    .lr-apply-modal { width:min(880px, 100%); max-height:min(90vh, 820px); display:flex; flex-direction:column;
      background:#0E0F14; border:.5px solid rgba(255,255,255,.08); border-radius:24px; overflow:hidden;
      box-shadow:0 30px 80px rgba(0,0,0,.6); animation:lrSlide .22s ease-out; color:#EFEEEC; font-family:'Geist','Nexa',sans-serif; }

    .lr-apply-head { display:flex; justify-content:space-between; align-items:center; padding:20px 28px;
      border-bottom:.5px solid rgba(255,255,255,.06); flex-shrink:0; }
    .lr-apply-head .step { font-size:11px; letter-spacing:.18em; text-transform:uppercase; color:rgba(239,238,236,.55); }
    .lr-apply-head .x { background:transparent; border:0; color:rgba(239,238,236,.55); font-size:24px; cursor:pointer;
      width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center;
      transition:background .15s, color .15s; }
    .lr-apply-head .x:hover { background:rgba(255,255,255,.06); color:#EFEEEC; }

    .lr-apply-body { padding:32px 28px; overflow-y:auto; flex:1; }
    .lr-apply-body h2 { font-family:'Nexa','Geist',sans-serif; font-weight:300; font-size:36px; line-height:1.05;
      letter-spacing:-.02em; margin:0 0 12px 0; }
    .lr-apply-body h2 em { color:#3FCF3F; font-style:italic; }
    .lr-apply-body p.sub { color:rgba(239,238,236,.65); font-size:14px; line-height:1.5; margin:0; max-width:60ch; }

    .lr-apply-foot { display:flex; justify-content:space-between; align-items:center; gap:12px;
      padding:20px 28px; border-top:.5px solid rgba(255,255,255,.06); flex-shrink:0; }
    .lr-apply-foot .back { background:transparent; border:0; color:rgba(239,238,236,.6); cursor:pointer;
      font-size:14px; padding:10px 14px; border-radius:10px; transition:color .15s, background .15s; }
    .lr-apply-foot .back:hover { color:#EFEEEC; background:rgba(255,255,255,.05); }
    .lr-apply-foot .primary { background:#3FCF3F; color:#0A0A0E; border:0; padding:14px 22px; border-radius:999px;
      font-weight:600; font-size:14px; cursor:pointer; transition:transform .15s, box-shadow .15s, opacity .15s; }
    .lr-apply-foot .primary:hover:not(:disabled) { transform:translateY(-1px); box-shadow:0 8px 24px rgba(63,207,63,.35); }
    .lr-apply-foot .primary:disabled { opacity:.45; cursor:not-allowed; }

    /* Selector */
    .lr-sel-opts { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:28px; }
    .lr-sel-opt { text-align:left; background:rgba(255,255,255,.03); border:.5px solid rgba(255,255,255,.08);
      border-radius:18px; padding:24px; cursor:pointer; transition:transform .15s, border-color .15s, background .15s;
      color:inherit; font:inherit; display:flex; flex-direction:column; gap:12px; }
    .lr-sel-opt:hover { transform:translateY(-2px); border-color:rgba(63,207,63,.55); background:rgba(63,207,63,.05); }
    .lr-sel-opt .tag { display:inline-flex; align-self:flex-start; padding:5px 12px; border-radius:999px;
      background:rgba(63,207,63,.12); color:#3FCF3F; font-size:11px; letter-spacing:.1em; text-transform:uppercase; }
    .lr-sel-opt h3 { margin:0; font-family:'Nexa','Geist',sans-serif; font-weight:300; font-size:22px; line-height:1.2;
      letter-spacing:-.01em; }
    .lr-sel-opt p { margin:0; color:rgba(239,238,236,.6); font-size:13px; line-height:1.5; }

    /* Form */
    .lr-form-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px 24px; margin-top:24px; }
    .lr-form-grid .full { grid-column:1 / -1; }
    .lr-field { display:flex; flex-direction:column; gap:6px; }
    .lr-field label { font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:rgba(239,238,236,.55); }
    .lr-field label .req { color:#3FCF3F; }
    .lr-field input, .lr-field select, .lr-field textarea {
      background:transparent; border:0; border-bottom:1px solid rgba(255,255,255,.12);
      color:#EFEEEC; font:inherit; font-size:16px; padding:10px 0; outline:none;
      font-family:'Geist','Nexa',sans-serif; width:100%; transition:border-color .15s; }
    .lr-field input::placeholder, .lr-field textarea::placeholder { color:rgba(239,238,236,.3); }
    .lr-field input:focus, .lr-field select:focus, .lr-field textarea:focus { border-bottom-color:#3FCF3F; }
    .lr-field select { appearance:none; -webkit-appearance:none; background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8' fill='none'><path d='M1 1.5L6 6.5L11 1.5' stroke='%23EFEEEC' stroke-opacity='0.55' stroke-width='1.2'/></svg>");
      background-repeat:no-repeat; background-position:right 4px center; padding-right:24px; cursor:pointer; }
    .lr-field select option { background:#0E0F14; color:#EFEEEC; }
    .lr-field textarea { resize:vertical; min-height:80px; }
    .lr-field.err input, .lr-field.err select, .lr-field.err textarea { border-bottom-color:#ff6b6b; }

    /* Calendar */
    .lr-cal { display:grid; grid-template-columns:1.1fr .9fr; gap:32px; margin-top:24px; }
    .lr-cal-side { display:flex; flex-direction:column; gap:18px; }
    .lr-cal-nav { display:flex; justify-content:space-between; align-items:center; }
    .lr-cal-nav .mlabel { font-family:'Nexa','Geist',sans-serif; font-weight:300; font-size:18px; letter-spacing:-.01em;
      text-transform:capitalize; }
    .lr-cal-nav button { background:rgba(255,255,255,.05); border:0; color:#EFEEEC; width:32px; height:32px;
      border-radius:10px; cursor:pointer; font-size:16px; transition:background .15s; }
    .lr-cal-nav button:hover:not(:disabled) { background:rgba(255,255,255,.1); }
    .lr-cal-nav button:disabled { opacity:.3; cursor:not-allowed; }

    .lr-cal-grid { display:grid; grid-template-columns:repeat(7, 1fr); gap:4px; }
    .lr-cal-dow { font-size:10px; color:rgba(239,238,236,.4); text-transform:uppercase; text-align:center;
      letter-spacing:.1em; padding:8px 0; }
    .lr-cal-day { aspect-ratio:1; display:flex; align-items:center; justify-content:center; border:0;
      background:transparent; color:#EFEEEC; font:inherit; font-size:14px; border-radius:10px; cursor:pointer;
      transition:background .12s, color .12s; }
    .lr-cal-day:hover:not(:disabled):not(.selected) { background:rgba(255,255,255,.08); }
    .lr-cal-day.other { color:rgba(239,238,236,.15); }
    .lr-cal-day:disabled { color:rgba(239,238,236,.2); cursor:not-allowed; }
    .lr-cal-day.selected { background:#3FCF3F; color:#0A0A0E; font-weight:600; }
    .lr-cal-day.today:not(.selected) { box-shadow:inset 0 0 0 1px rgba(63,207,63,.5); }

    .lr-cal-slots-head { font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:rgba(239,238,236,.55); }
    .lr-cal-slots-sub { font-size:13px; color:rgba(239,238,236,.5); margin-top:-10px; }
    .lr-cal-slots { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
    .lr-cal-slot { background:rgba(255,255,255,.05); border:.5px solid rgba(255,255,255,.08); color:#EFEEEC;
      padding:12px; border-radius:10px; font:inherit; font-size:14px; cursor:pointer;
      transition:transform .12s, border-color .12s, background .12s; }
    .lr-cal-slot:hover { transform:translateY(-1px); border-color:rgba(63,207,63,.5); }
    .lr-cal-slot.on { background:#3FCF3F; color:#0A0A0E; border-color:#3FCF3F; font-weight:600; }
    .lr-cal-empty { color:rgba(239,238,236,.5); font-size:13px; padding:24px; text-align:center;
      background:rgba(255,255,255,.03); border-radius:12px; }

    /* Done / error */
    .lr-done { padding:40px 28px; text-align:center; display:flex; flex-direction:column; gap:16px; align-items:center; }
    .lr-done .ic { width:64px; height:64px; border-radius:50%; background:rgba(63,207,63,.15); color:#3FCF3F;
      display:flex; align-items:center; justify-content:center; font-size:32px; font-weight:300; }
    .lr-done.is-err .ic { background:rgba(255,107,107,.15); color:#ff6b6b; }
    .lr-done h3 { font-family:'Nexa','Geist',sans-serif; font-weight:300; font-size:28px; margin:0; letter-spacing:-.01em; }
    .lr-done p { color:rgba(239,238,236,.65); font-size:14px; max-width:42ch; margin:0; line-height:1.5; }
    .lr-done .meet { display:inline-flex; gap:8px; align-items:center; padding:12px 20px; border-radius:999px;
      background:rgba(63,207,63,.12); color:#3FCF3F; font-size:14px; text-decoration:none; margin-top:8px; }
    .lr-done .meet:hover { background:rgba(63,207,63,.2); }

    /* Mobile */
    @media (max-width:760px) {
      .lr-apply-overlay { padding:0; align-items:stretch; }
      .lr-apply-modal { width:100%; max-height:100vh; border-radius:0; }
      .lr-apply-body { padding:24px 20px; }
      .lr-apply-head { padding:16px 20px; }
      .lr-apply-foot { padding:16px 20px; }
      .lr-apply-body h2 { font-size:28px; }
      .lr-sel-opts { grid-template-columns:1fr; }
      .lr-form-grid { grid-template-columns:1fr; gap:18px; }
      .lr-cal { grid-template-columns:1fr; gap:24px; }
    }
  `;

  // Initial form state per type
  function emptyForm(type) {
    const common = { name: '', email: '', phone: '', brand: '', website: '' };
    if (type === 'partner') {
      return { ...common, category: '', time_selling: '', revenue: '', ad_spend: '', has_agency: '', goal: '' };
    }
    return { ...common, stage: '', what_you_sell: '', revenue: '', tried: '', goal: '' };
  }

  // Required fields per type (everything that is asked must be filled)
  const REQUIRED = {
    partner: ['name', 'email', 'phone', 'brand', 'website', 'category', 'time_selling', 'revenue', 'ad_spend', 'has_agency', 'goal'],
    advisor: ['name', 'email', 'phone', 'brand', 'website', 'stage', 'what_you_sell', 'revenue', 'tried', 'goal'],
  };

  // ------- Components -------

  function Selector({ lang, onPick, onClose }) {
    const T = window.CONTENT.apply.selector;
    return (
      <>
        <div className="lr-apply-head">
          <span className="step">{lang === 'es' ? 'Elige tu camino' : 'Choose your path'}</span>
          <button className="x" onClick={onClose} aria-label="Close">×</button>
        </div>
        <div className="lr-apply-body">
          <h2>{T.title[lang]}</h2>
          <p className="sub">{T.sub[lang]}</p>
          <div className="lr-sel-opts">
            {['partner', 'advisor'].map((k) => {
              const o = T.options[k];
              return (
                <button key={k} className="lr-sel-opt" onClick={() => onPick(k)}>
                  <span className="tag">{o.tag[lang]}</span>
                  <h3>{o.title[lang]}</h3>
                  <p>{o.desc[lang]}</p>
                </button>
              );
            })}
          </div>
        </div>
      </>
    );
  }

  function FormField({ name, conf, lang, value, onChange, error }) {
    const label = (
      <label htmlFor={`lr-${name}`}>
        {conf.label[lang]} <span className="req">*</span>
      </label>
    );
    if (conf.options) {
      return (
        <div className={`lr-field ${error ? 'err' : ''}`}>
          {label}
          <select id={`lr-${name}`} value={value} onChange={(e) => onChange(name, e.target.value)}>
            {conf.options[lang].map((o, i) =>
              <option key={i} value={i === 0 ? '' : o} disabled={i === 0}>{o}</option>
            )}
          </select>
        </div>
      );
    }
    const isTextarea = name === 'goal' || name === 'tried' || name === 'what_you_sell';
    return (
      <div className={`lr-field ${error ? 'err' : ''}`}>
        {label}
        {isTextarea
          ? <textarea id={`lr-${name}`} placeholder={conf.ph?.[lang] || ''} value={value} onChange={(e) => onChange(name, e.target.value)} rows={3} />
          : <input id={`lr-${name}`} type={name === 'email' ? 'email' : 'text'} placeholder={conf.ph?.[lang] || ''} value={value} onChange={(e) => onChange(name, e.target.value)} />
        }
      </div>
    );
  }

  function Form({ lang, type, data, setData, errors, onClose, onBack, onNext }) {
    const T = window.CONTENT.apply[type];
    const common = window.CONTENT.apply.common;
    const order = type === 'partner'
      ? ['name', 'email', 'phone', 'brand', 'website', 'category', 'time_selling', 'revenue', 'ad_spend', 'has_agency', 'goal']
      : ['name', 'email', 'phone', 'brand', 'website', 'stage', 'what_you_sell', 'revenue', 'tried', 'goal'];

    const update = useCallback((k, v) => setData((d) => ({ ...d, [k]: v })), [setData]);

    return (
      <>
        <div className="lr-apply-head">
          <span className="step">{common.step_form[lang]}</span>
          <button className="x" onClick={onClose} aria-label="Close">×</button>
        </div>
        <div className="lr-apply-body">
          <h2>{T.title[lang]}</h2>
          <p className="sub">{T.sub[lang]}</p>
          <div className="lr-form-grid">
            {order.map((name) => {
              const isFull = ['goal', 'tried', 'what_you_sell', 'website'].includes(name);
              return (
                <div key={name} className={isFull ? 'full' : ''}>
                  <FormField
                    name={name}
                    conf={T.fields[name]}
                    lang={lang}
                    value={data[name] || ''}
                    onChange={update}
                    error={errors[name]}
                  />
                </div>
              );
            })}
          </div>
        </div>
        <div className="lr-apply-foot">
          <button className="back" onClick={onBack}>{common.back[lang]}</button>
          <button className="primary" onClick={onNext}>{common.submit_and_book[lang]}</button>
        </div>
      </>
    );
  }

  function Calendar({ lang, onClose, onBack, onConfirm, submitting }) {
    const T = window.CONTENT.apply.calendar;
    const common = window.CONTENT.apply.common;
    const [month, setMonth] = useState(() => startOfMonth(new Date()));
    const [date, setDate] = useState(null);
    const [time, setTime] = useState(null);
    const [slots, setSlots] = useState([]);
    const [loadingSlots, setLoadingSlots] = useState(false);
    const today = useMemo(() => { const t = new Date(); t.setHours(0,0,0,0); return t; }, []);
    const maxMonth = useMemo(() => addMonths(today, 3), [today]); // up to 3 months ahead

    const days = useMemo(() => buildMonthGrid(month), [month]);
    const currentMonthIdx = month.getMonth();

    // Fetch slots when date changes
    useEffect(() => {
      if (!date) { setSlots([]); return; }
      let cancelled = false;
      setLoadingSlots(true);
      setTime(null);
      const dateStr = fmtDateISO(date);
      fetch(`/api/get-availability?date=${dateStr}`)
        .then((r) => r.ok ? r.json() : Promise.reject(r))
        .then((d) => { if (!cancelled) setSlots(d.available_slots || d.slots || []); })
        .catch(() => { if (!cancelled) setSlots([]); })
        .finally(() => { if (!cancelled) setLoadingSlots(false); });
      return () => { cancelled = true; };
    }, [date]);

    const canPrev = startOfMonth(month) > startOfMonth(today);
    const canNext = startOfMonth(month) < maxMonth;

    return (
      <>
        <div className="lr-apply-head">
          <span className="step">{common.step_calendar[lang]}</span>
          <button className="x" onClick={onClose} aria-label="Close">×</button>
        </div>
        <div className="lr-apply-body">
          <h2>{T.title[lang]}</h2>
          <p className="sub">{T.sub[lang]}</p>
          <div className="lr-cal">
            <div>
              <div className="lr-cal-nav">
                <button onClick={() => setMonth(addMonths(month, -1))} disabled={!canPrev} aria-label="Prev">‹</button>
                <span className="mlabel">{monthLabel(month, lang)}</span>
                <button onClick={() => setMonth(addMonths(month, 1))} disabled={!canNext} aria-label="Next">›</button>
              </div>
              <div className="lr-cal-grid">
                {(lang === 'es' ? ['L','M','X','J','V','S','D'] : ['M','T','W','T','F','S','S']).map((d, i) =>
                  <div key={`dow-${i}`} className="lr-cal-dow">{d}</div>
                )}
                {days.map((d, i) => {
                  const isOther = d.getMonth() !== currentMonthIdx;
                  const isPast = d < today;
                  const weekend = isWeekend(d);
                  const isSelected = date && fmtDateISO(d) === fmtDateISO(date);
                  const isToday = fmtDateISO(d) === fmtDateISO(today);
                  const disabled = isPast || weekend || isOther;
                  return (
                    <button
                      key={i}
                      className={`lr-cal-day ${isOther ? 'other' : ''} ${isSelected ? 'selected' : ''} ${isToday ? 'today' : ''}`}
                      disabled={disabled}
                      onClick={() => setDate(d)}>
                      {d.getDate()}
                    </button>
                  );
                })}
              </div>
            </div>
            <div className="lr-cal-side">
              <span className="lr-cal-slots-head">{T.pick_time[lang]}</span>
              {!date && <div className="lr-cal-empty">{T.pick_date[lang]}</div>}
              {date && loadingSlots && <div className="lr-cal-empty">{T.loading[lang]}</div>}
              {date && !loadingSlots && slots.length === 0 && <div className="lr-cal-empty">{T.no_slots[lang]}</div>}
              {date && !loadingSlots && slots.length > 0 && (
                <div className="lr-cal-slots">
                  {slots.map((s) =>
                    <button key={s} className={`lr-cal-slot ${time === s ? 'on' : ''}`} onClick={() => setTime(s)}>
                      {fmtTimeLabel(s, lang)}
                    </button>
                  )}
                </div>
              )}
              {date && (
                <span className="lr-cal-slots-sub">{T.timezone_note[lang]}</span>
              )}
            </div>
          </div>
        </div>
        <div className="lr-apply-foot">
          <button className="back" onClick={onBack} disabled={submitting}>{common.back[lang]}</button>
          <button
            className="primary"
            disabled={!date || !time || submitting}
            onClick={() => onConfirm({ date: fmtDateISO(date), time })}>
            {submitting ? common.booking[lang] : T.confirm[lang]}
          </button>
        </div>
      </>
    );
  }

  function Done({ lang, onClose, result }) {
    const c = window.CONTENT.apply.common;
    return (
      <div className="lr-done">
        <div className="ic">✓</div>
        <h3>{c.submitted_title[lang]}</h3>
        <p>{c.submitted_sub[lang]}</p>
        {result?.meetLink && (
          <a className="meet" href={result.meetLink} target="_blank" rel="noopener noreferrer">
            Google Meet →
          </a>
        )}
        <div style={{ marginTop: 12 }}>
          <button className="primary" onClick={onClose} style={{ background:'#3FCF3F', color:'#0A0A0E', border:0, padding:'12px 24px', borderRadius:999, cursor:'pointer', fontWeight:600 }}>
            {c.submitted_close[lang]}
          </button>
        </div>
      </div>
    );
  }

  function Err({ lang, onRetry, onClose, message }) {
    const c = window.CONTENT.apply.common;
    return (
      <div className="lr-done is-err">
        <div className="ic">!</div>
        <h3>{c.error_title[lang]}</h3>
        <p>{message || c.error_sub[lang]}</p>
        <div style={{ marginTop: 12, display:'flex', gap:12 }}>
          <button className="back" onClick={onClose} style={{ background:'transparent', border:0, color:'rgba(239,238,236,.6)', cursor:'pointer', padding:'12px 18px' }}>
            {c.submitted_close[lang]}
          </button>
          <button className="primary" onClick={onRetry} style={{ background:'#3FCF3F', color:'#0A0A0E', border:0, padding:'12px 24px', borderRadius:999, cursor:'pointer', fontWeight:600 }}>
            {c.error_retry[lang]}
          </button>
        </div>
      </div>
    );
  }

  // ------- Modal root -------
  function ApplyModal({ lang }) {
    const [state, setState] = useState({ open: false, step: 'selector', type: null });
    const [data, setData] = useState({});
    const [errors, setErrors] = useState({});
    const [submitting, setSubmitting] = useState(false);
    const [result, setResult] = useState(null);
    const [errMessage, setErrMessage] = useState('');
    const initialized = useRef(false);

    // Register the bridge so external buttons can open us
    useEffect(() => {
      setOpenState = (s) => {
        setState(s);
        // Reset form fresh when opening a new type
        if (s.open && s.type) {
          setData(emptyForm(s.type));
          setErrors({});
          setResult(null);
          setErrMessage('');
        }
        if (s.open && s.step === 'selector') {
          setData({});
          setErrors({});
          setResult(null);
          setErrMessage('');
        }
      };
      return () => { setOpenState = null; };
    }, []);

    // ESC to close + lock body scroll
    useEffect(() => {
      if (!state.open) return;
      const onKey = (e) => { if (e.key === 'Escape') close(); };
      window.addEventListener('keydown', onKey);
      const prev = document.body.style.overflow;
      document.body.style.overflow = 'hidden';
      return () => { window.removeEventListener('keydown', onKey); document.body.style.overflow = prev; };
    }, [state.open]);

    const pickType = (type) => {
      setData(emptyForm(type));
      setErrors({});
      setState((s) => ({ ...s, step: 'form', type }));
    };

    const goSelector = () => setState((s) => ({ ...s, step: 'selector', type: null }));
    const goCalendar = () => {
      // Validate the active form
      const req = REQUIRED[state.type] || [];
      const next = {};
      for (const k of req) { if (!data[k] || String(data[k]).trim() === '') next[k] = true; }
      // Email shape check
      if (data.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) next.email = true;
      setErrors(next);
      if (Object.keys(next).length > 0) {
        // Scroll modal body to top so user sees first error
        document.querySelector('.lr-apply-body')?.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      setState((s) => ({ ...s, step: 'calendar' }));
    };

    const goForm = () => setState((s) => ({ ...s, step: 'form' }));

    const confirm = async ({ date, time }) => {
      setSubmitting(true);
      setErrMessage('');
      try {
        const payload = {
          ...data,
          date,
          time,
          applyType: state.type, // partner | advisor
          lang,
        };
        const res = await fetch('/api/book-appointment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        if (!res.ok) {
          const e = await res.json().catch(() => ({}));
          throw new Error(e.error || `HTTP ${res.status}`);
        }
        const j = await res.json();
        setResult(j);
        setState((s) => ({ ...s, step: 'done' }));
      } catch (e) {
        setErrMessage(e.message || '');
        setState((s) => ({ ...s, step: 'error' }));
      } finally {
        setSubmitting(false);
      }
    };

    // Mount styles once
    useEffect(() => {
      if (initialized.current) return;
      initialized.current = true;
      const tag = document.createElement('style');
      tag.id = 'lr-apply-styles';
      tag.textContent = STYLES;
      document.head.appendChild(tag);
    }, []);

    if (!state.open) return null;

    return (
      <div className="lr-apply-overlay" onClick={(e) => { if (e.target.classList.contains('lr-apply-overlay')) close(); }}>
        <div className="lr-apply-modal" role="dialog" aria-modal="true">
          {state.step === 'selector' && (
            <Selector lang={lang} onPick={pickType} onClose={close} />
          )}
          {state.step === 'form' && (
            <Form
              lang={lang}
              type={state.type}
              data={data}
              setData={setData}
              errors={errors}
              onClose={close}
              onBack={goSelector}
              onNext={goCalendar}
            />
          )}
          {state.step === 'calendar' && (
            <Calendar
              lang={lang}
              onClose={close}
              onBack={goForm}
              onConfirm={confirm}
              submitting={submitting}
            />
          )}
          {state.step === 'done' && (
            <Done lang={lang} onClose={close} result={result} />
          )}
          {state.step === 'error' && (
            <Err lang={lang} onClose={close} onRetry={goForm} message={errMessage} />
          )}
        </div>
      </div>
    );
  }

  window.D3Apply = { Modal: ApplyModal, openSelector, openForm, close };
})();
