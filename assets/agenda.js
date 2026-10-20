// LA REAL — Agenda: formulario corto + día y hora + confirmación.
// Solo se agenda desde un servicio: cada botón [data-book="Servicio"] abre el modal con ese servicio fijo.
// Disponibilidad y reserva: /api/get-availability y /api/book-appointment (Google Calendar).
(() => {
  const REVENUE = ['Aún no vendo online', 'Menos de $20M al mes', '$20M a $50M al mes', '$50M a $150M al mes', '$150M a $500M al mes', 'Más de $500M al mes'];
  const AD_SPEND = ['No invierto todavía', 'Menos de $3M al mes', '$3M a $5M al mes', '$5M a $15M al mes', 'Más de $15M al mes'];
  const FIELDS = [
    { k: 'name', label: 'Nombre', type: 'text', auto: 'name' },
    { k: 'email', label: 'Correo', type: 'email', auto: 'email' },
    { k: 'phone', label: 'Celular', type: 'tel', auto: 'tel' },
    { k: 'brand', label: 'Marca', type: 'text', auto: 'organization' },
    { k: 'website', label: 'Sitio web o Instagram', type: 'text', full: true, auto: 'url' },
    { k: 'revenue', label: 'Ventas online al mes', options: REVENUE },
    { k: 'ad_spend', label: 'Inversión en anuncios al mes', options: AD_SPEND },
    { k: 'goal', label: '¿Qué quieres resolver?', textarea: true, full: true },
  ];
  const DOW = ['dom', 'lun', 'mar', 'mié', 'jue', 'vie', 'sáb'];
  const MONTHS = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
  const ICON_X = '<svg viewBox="0 0 14 14" fill="none"><path d="M1 1l12 12M13 1L1 13" stroke="currentColor" stroke-width="1.5"/></svg>';
  const ICON_OK = '<svg viewBox="0 0 22 22" fill="none"><path d="M4 11.5l4.5 4.5L18 6.5" stroke="currentColor" stroke-width="2"/></svg>';

  const state = { step: 'form', data: { service: '' }, day: null, time: null, result: null };
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  // Fechas en hora de Bogotá (UTC-5), sin depender de la zona del visitante
  function bogotaDate(offsetDays) {
    const d = new Date(Date.now() - 5 * 3600e3 + offsetDays * 86400e3);
    return { iso: d.toISOString().slice(0, 10), dow: d.getUTCDay(), day: d.getUTCDate(), month: d.getUTCMonth() };
  }
  function workDays(n) {
    const out = [];
    for (let i = 0; out.length < n && i < 40; i++) {
      const d = bogotaDate(i);
      if (d.dow !== 0 && d.dow !== 6) out.push(d);
    }
    return out;
  }
  function timeLabel(t) {
    const [h, m] = t.split(':').map(Number);
    return `${((h + 11) % 12) + 1}:${String(m).padStart(2, '0')} ${h < 12 ? 'a. m.' : 'p. m.'}`;
  }
  function dayLabel(iso) {
    return new Date(`${iso}T12:00:00-05:00`).toLocaleDateString('es-CO', { weekday: 'long', day: 'numeric', month: 'long', timeZone: 'America/Bogota' });
  }

  // ---------- Modal ----------
  const root = document.createElement('div');
  root.className = 'ag';
  root.hidden = true;
  root.innerHTML = '<div class="ag-panel" role="dialog" aria-modal="true" aria-labelledby="ag-title"></div>';
  document.body.appendChild(root);
  const panel = root.firstElementChild;
  let lastFocus = null;

  function open(service) {
    lastFocus = document.activeElement;
    if (!service) return;
    if (state.step === 'done') reset();
    // Si cambia de servicio se conservan los datos, pero vuelve al paso 1
    if (state.data.service !== service) { state.data.service = service; state.step = 'form'; state.time = null; }
    render();
    root.hidden = false;
    document.body.classList.add('ag-lock');
    requestAnimationFrame(() => root.classList.add('open'));
    panel.querySelector('.ag-close').focus({ preventScroll: true });
  }
  function close() {
    root.classList.remove('open');
    document.body.classList.remove('ag-lock');
    setTimeout(() => { root.hidden = true; }, 250);
    lastFocus && lastFocus.focus({ preventScroll: true });
  }
  function reset() {
    state.step = 'form'; state.data = { service: '' }; state.day = null; state.time = null; state.result = null;
  }

  root.addEventListener('click', (e) => { if (e.target === root) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !root.hidden) close(); });
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-book]');
    if (b) { e.preventDefault(); open(b.dataset.book); }
  });

  function head(stepText) {
    return `<div class="ag-head"><span class="label">${stepText}</span><button class="ag-close" type="button" aria-label="Cerrar">${ICON_X}</button></div>`;
  }

  function render() {
    if (state.step === 'form') renderForm();
    else if (state.step === 'time') renderTime();
    else renderDone();
    panel.querySelector('.ag-close').addEventListener('click', close);
    panel.scrollTop = 0;
  }

  // ---------- Paso 1: datos ----------
  function renderForm() {
    const d = state.data;
    panel.innerHTML = `${head('Paso 1 de 2')}
      <p class="ag-svc">${esc(d.service)}</p>
      <h3 id="ag-title">Agenda una llamada <b>con Juanfe.</b></h3>
      <p class="ag-sub">Videollamada de 30 minutos. Cuéntanos de tu marca para llegar preparados.</p>
      <form class="ag-section ag-fields" novalidate>
        ${FIELDS.map((f) => {
          const v = esc(d[f.k] || '');
          const ctl = f.options
            ? `<select id="ag-${f.k}" name="${f.k}"><option value="">Elige una opción</option>${f.options.map((o) => `<option${d[f.k] === o ? ' selected' : ''}>${esc(o)}</option>`).join('')}</select>`
            : f.textarea
              ? `<textarea id="ag-${f.k}" name="${f.k}" placeholder="Ej: vendemos bien en tienda física y queremos crecer online">${v}</textarea>`
              : `<input id="ag-${f.k}" name="${f.k}" type="${f.type}" value="${v}" autocomplete="${f.auto}"${f.type === 'tel' ? ' inputmode="tel"' : ''}>`;
          return `<div class="ag-field${f.full ? ' full' : ''}" data-f="${f.k}"><label for="ag-${f.k}">${f.label}</label>${ctl}<p class="ag-msg">Completa este campo.</p></div>`;
        }).join('')}
      </form>
      <div class="ag-actions"><button class="btn btn-dark" type="button" data-next>Elegir día y hora</button></div>`;

    const form = panel.querySelector('form');
    form.addEventListener('input', (e) => {
      state.data[e.target.name] = e.target.value;
      e.target.closest('.ag-field').classList.remove('err');
    });
    form.addEventListener('submit', (e) => e.preventDefault());
    panel.querySelector('[data-next]').addEventListener('click', () => {
      let first = null;
      const bad = (k) => { const el = panel.querySelector(`[data-f="${k}"]`); el.classList.add('err'); first = first || el; };
      FIELDS.forEach((f) => {
        const v = (state.data[f.k] || '').trim();
        if (!v || (f.k === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) || (f.k === 'phone' && v.replace(/\D/g, '').length < 7)) bad(f.k);
      });
      if (first) { first.scrollIntoView({ block: 'center', behavior: 'smooth' }); return; }
      state.step = 'time';
      window.fbq && fbq('track', 'Lead', { content_name: state.data.service });
      render();
    });
  }

  // ---------- Paso 2: día y hora ----------
  const cache = {};
  function renderTime(alert) {
    const days = workDays(15);
    if (!state.day) state.day = days[0].iso;
    panel.innerHTML = `${head('Paso 2 de 2')}
      <p class="ag-svc">${esc(state.data.service)}</p>
      <h3 id="ag-title">Elige <b>día y hora.</b></h3>
      <p class="ag-sub">Hora de Colombia (GMT-5). La llamada dura 30 minutos.</p>
      <div class="ag-section"><span class="label">Día</span>
        <div class="ag-days">${days.map((d) => `<button type="button" class="ag-day" data-day="${d.iso}" aria-pressed="${state.day === d.iso}"><small>${DOW[d.dow]}</small><b>${d.day}</b><span>${MONTHS[d.month]}</span></button>`).join('')}</div>
      </div>
      <div class="ag-section"><span class="label">Hora</span><div class="ag-slots" aria-live="polite"></div></div>
      ${alert ? `<div class="ag-alert">${esc(alert)}</div>` : ''}
      <div class="ag-actions"><button class="btn btn-dark" type="button" data-confirm disabled>Confirmar cita</button><button class="ag-back" type="button" data-back>Volver a mis datos</button></div>`;

    panel.querySelectorAll('[data-day]').forEach((b) => b.addEventListener('click', () => {
      state.day = b.dataset.day; state.time = null;
      panel.querySelectorAll('[data-day]').forEach((x) => x.setAttribute('aria-pressed', x === b));
      loadSlots();
    }));
    panel.querySelector('[data-back]').addEventListener('click', () => { state.step = 'form'; render(); });
    panel.querySelector('[data-confirm]').addEventListener('click', confirm);
    panel.querySelector(`[data-day="${state.day}"]`)?.scrollIntoView({ inline: 'center', block: 'nearest' });
    loadSlots();
  }

  async function loadSlots(autoAdvance = true) {
    const box = panel.querySelector('.ag-slots');
    const day = state.day;
    box.innerHTML = '<div class="ag-skel"></div>'.repeat(6);
    updateConfirm();
    let slots = cache[day];
    if (!slots) {
      try {
        const r = await fetch(`/api/get-availability?date=${day}`);
        if (!r.ok) throw new Error();
        slots = (await r.json()).available_slots || [];
        cache[day] = slots;
      } catch {
        if (state.day === day) box.innerHTML = '<p class="ag-note">No pudimos cargar la agenda. Intenta de nuevo en un momento.</p>';
        return;
      }
    }
    if (state.day !== day) return;
    // Si el primer día ya no tiene cupos, saltamos solos al siguiente
    if (!slots.length && autoAdvance) {
      const btns = [...panel.querySelectorAll('[data-day]')];
      const i = btns.findIndex((b) => b.dataset.day === day);
      if (i === 0 && btns[1]) { btns[1].click(); return; }
    }
    box.innerHTML = slots.length
      ? slots.map((t) => `<button type="button" class="ag-slot" data-time="${t}" aria-pressed="${state.time === t}">${timeLabel(t)}</button>`).join('')
      : '<p class="ag-note">No hay horarios libres este día. Prueba con otro.</p>';
    box.querySelectorAll('[data-time]').forEach((b) => b.addEventListener('click', () => {
      state.time = b.dataset.time;
      box.querySelectorAll('[data-time]').forEach((x) => x.setAttribute('aria-pressed', x === b));
      updateConfirm();
    }));
  }

  function updateConfirm() {
    const b = panel.querySelector('[data-confirm]');
    if (b) b.disabled = !state.time;
  }

  async function confirm() {
    const b = panel.querySelector('[data-confirm]');
    b.disabled = true; b.textContent = 'Agendando…';
    try {
      const r = await fetch('/api/book-appointment', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ applyType: 'service', ...state.data, date: state.day, time: state.time }),
      });
      const json = await r.json().catch(() => ({}));
      if (r.status === 409) {
        delete cache[state.day]; state.time = null;
        renderTime(json.error || 'Ese horario se acaba de ocupar. Elige otro.');
        return;
      }
      if (!r.ok || !json.success) throw new Error();
      state.result = json; state.step = 'done';
      window.fbq && fbq('track', 'Schedule', { content_name: state.data.service });
      render();
    } catch {
      b.disabled = false; b.textContent = 'Confirmar cita';
      if (!panel.querySelector('.ag-alert')) b.closest('.ag-actions').insertAdjacentHTML('beforebegin', '<div class="ag-alert">No pudimos agendar la cita. Intenta de nuevo o escríbenos a juanfe@larealmarketing.com.</div>');
    }
  }

  // ---------- Confirmación ----------
  function renderDone() {
    const { data, day, time, result } = state;
    const start = new Date(`${day}T${time}:00-05:00`);
    const end = new Date(start.getTime() + 30 * 60e3);
    const fmt = (d) => d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    const gcal = 'https://calendar.google.com/calendar/render?action=TEMPLATE'
      + `&text=${encodeURIComponent(`Llamada con LA REAL · ${data.service}`)}`
      + `&dates=${fmt(start)}/${fmt(end)}`
      + `&details=${encodeURIComponent(`Videollamada con Juanfe: ${result.meetLink}`)}`
      + `&location=${encodeURIComponent(result.meetLink)}`;
    panel.innerHTML = `${head('Cita confirmada')}
      <div class="ag-done">
        <div class="ag-check">${ICON_OK}</div>
        <h3 id="ag-title">Listo, <b>${esc(data.name.split(' ')[0])}.</b></h3>
        <p class="ag-sub">Tu llamada con Juanfe quedó agendada.</p>
        <div class="ag-when"><b>${esc(dayLabel(day))} · ${timeLabel(time)}</b>Hora de Colombia<br><a href="${esc(result.meetLink)}" target="_blank" rel="noopener">${esc(result.meetLink)}</a></div>
      </div>
      <div class="ag-actions"><a class="btn btn-dark" href="${gcal}" target="_blank" rel="noopener">Agregar a mi calendario</a><button class="ag-back" type="button" data-done>Cerrar</button></div>`;
    panel.querySelector('[data-done]').addEventListener('click', close);
  }
})();
