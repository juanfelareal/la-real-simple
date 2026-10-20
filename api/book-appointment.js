// LA REAL — Book appointment endpoint
// Recibe la solicitud de un servicio (o las aplicaciones viejas "partner"/"advisor") + fecha/hora.
// Vuelve a revisar que el horario siga libre en los calendarios de Juanfe, crea el evento
// en cada calendario con permiso de escritura y agrega una fila a Google Sheets.

const {
  CONFIG, eventCalendarIds, hasCredentials, isMockMode, getClients,
  slotStart, isBookableDate, busyPeriods, freeSlots,
} = require('./_calendar');

const REQUIRED = {
  service: ['service', 'name', 'email', 'phone', 'brand', 'website', 'revenue', 'goal'],
  partner: ['name', 'email', 'phone', 'brand', 'website', 'category', 'time_selling', 'revenue', 'ad_spend', 'has_agency', 'goal'],
  advisor: ['name', 'email', 'phone', 'brand', 'website', 'stage', 'what_you_sell', 'revenue', 'tried', 'goal'],
};

const LABELS = {
  name: 'Nombre', email: 'Email', phone: 'Teléfono', brand: 'Marca', website: 'URL / Instagram',
  revenue: 'Facturación mensual', ad_spend: 'Inversión mensual en pauta',
  category: 'Categoría', time_selling: 'Tiempo vendiendo online', has_agency: 'Trabaja con agencia hoy',
  stage: 'Etapa', what_you_sell: 'Qué vende', tried: 'Qué ha probado',
};

function typeLabel(body) {
  if (body.applyType === 'service') return body.service;
  return body.applyType === 'advisor' ? 'Growth Advisor' : 'Growth Partner';
}

function buildDescription(body) {
  const lines = [`SERVICIO`, `========`, typeLabel(body), ``, `INFORMACIÓN DEL LEAD`, `====================`];
  for (const [k, label] of Object.entries(LABELS)) {
    if (body[k]) lines.push(`${label}: ${body[k]}`);
  }
  lines.push(``, `QUÉ QUIERE RESOLVER`, `===================`, body.goal || '—',
    ``, `ENLACE DE VIDEOLLAMADA`, `======================`, CONFIG.meetLink);
  return lines.join('\n');
}

function rowForSheets(body, date, time, timestamp) {
  // Columnas A..R. Una sola hoja guarda todos los leads; algunas columnas quedan vacías según el tipo.
  const formattedDate = slotStart(date, time).toLocaleDateString('es-CO', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', timeZone: CONFIG.timezone,
  });
  return [
    timestamp,                 // A — Timestamp ISO
    typeLabel(body),           // B — Servicio / tipo
    body.name || '',           // C
    body.email || '',          // D
    body.phone || '',          // E
    body.brand || '',          // F
    body.website || '',        // G
    body.category || '',       // H — solo partner
    body.time_selling || '',   // I — solo partner
    body.revenue || '',        // J
    body.ad_spend || '',       // K
    body.has_agency || '',     // L — solo partner
    body.stage || '',          // M — solo advisor
    body.what_you_sell || '',  // N — solo advisor
    body.tried || '',          // O — solo advisor
    body.goal || '',           // P
    formattedDate,             // Q — fecha legible
    time,                      // R — hora
  ];
}

module.exports = async (req, res) => {
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const body = req.body || {};
    body.applyType = ['service', 'advisor'].includes(body.applyType) ? body.applyType : 'partner';
    const { date, time } = body;

    const required = [...REQUIRED[body.applyType], 'date', 'time'];
    const missing = required.filter((k) => !body[k] || String(body[k]).trim() === '');
    if (missing.length > 0) return res.status(400).json({ error: 'Missing required fields', missing });
    if (!isBookableDate(date) || !/^\d{2}:\d{2}$/.test(time)) return res.status(400).json({ error: 'Fecha u hora no válida' });

    if (isMockMode()) {
      return res.status(200).json({
        success: true, mode: 'development', eventId: 'dev-' + Date.now(),
        meetLink: CONFIG.meetLink, date, time,
      });
    }
    if (!hasCredentials()) return res.status(503).json({ error: 'Agenda no configurada' });

    const { calendar, sheets } = getClients();

    // El horario pudo ocuparse mientras la persona llenaba el formulario
    const busy = await busyPeriods(calendar, date);
    if (!freeSlots(date, busy).includes(time)) {
      return res.status(409).json({ error: 'Ese horario ya no está disponible. Elige otro.' });
    }

    const start = slotStart(date, time);
    const end = new Date(start.getTime() + CONFIG.slotDuration * 60000);
    const event = {
      summary: `LA REAL · ${typeLabel(body)} — ${body.name} (${body.brand})`,
      description: buildDescription(body),
      location: CONFIG.meetLink,
      start: { dateTime: start.toISOString(), timeZone: CONFIG.timezone },
      end: { dateTime: end.toISOString(), timeZone: CONFIG.timezone },
      reminders: { useDefault: false, overrides: [{ method: 'popup', minutes: 15 }] },
    };

    const created = [];
    for (const calendarId of eventCalendarIds()) {
      try {
        const r = await calendar.events.insert({ calendarId, resource: event });
        created.push({ calendarId, id: r.data.id });
      } catch (e) {
        console.error(`No se pudo crear el evento en ${calendarId}:`, e.message);
      }
    }
    if (created.length === 0) return res.status(500).json({ error: 'No se pudo crear la cita' });

    const sheetId = process.env.GOOGLE_SHEET_ID;
    if (sheetId) {
      try {
        await sheets.spreadsheets.values.append({
          spreadsheetId: sheetId,
          range: 'Leads!A:R',
          valueInputOption: 'USER_ENTERED',
          resource: { values: [rowForSheets(body, date, time, new Date().toISOString())] },
        });
      } catch (sheetError) {
        console.error('Error saving to Google Sheets:', sheetError);
        // Si falla Sheets, la cita igual queda creada
      }
    }

    return res.status(200).json({
      success: true, eventId: created[0].id, calendars: created.map((c) => c.calendarId),
      meetLink: CONFIG.meetLink, date, time,
    });
  } catch (err) {
    console.error('book-appointment error:', err);
    return res.status(500).json({ error: 'Internal error' });
  }
};
