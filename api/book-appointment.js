// LA REAL — Book appointment endpoint
// Accepts either a "partner" or "advisor" application + a date/time.
// Creates a Google Calendar event and appends a row to Google Sheets.

const { google } = require('googleapis');

const CONFIG = {
  slotDuration: 30, // minutes
  timezone: 'America/Bogota',
  meetLink: 'https://meet.google.com/jqb-ryky-kqx', // fixed Meet link
};

function getClients() {
  const auth = new google.auth.GoogleAuth({
    credentials: {
      client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
      private_key: process.env.GOOGLE_PRIVATE_KEY?.replace(/\\n/g, '\n'),
    },
    scopes: [
      'https://www.googleapis.com/auth/calendar',
      'https://www.googleapis.com/auth/spreadsheets',
    ],
  });
  return {
    calendar: google.calendar({ version: 'v3', auth }),
    sheets: google.sheets({ version: 'v4', auth }),
  };
}

// Required fields for each application type
const REQUIRED = {
  partner: ['name', 'email', 'phone', 'brand', 'website', 'category', 'time_selling', 'revenue', 'ad_spend', 'has_agency', 'goal'],
  advisor: ['name', 'email', 'phone', 'brand', 'website', 'stage', 'what_you_sell', 'revenue', 'tried', 'goal'],
};

function buildDescription(body) {
  const t = body.applyType === 'advisor' ? 'Growth Advisor' : 'Growth Partner';
  const lines = [
    `TIPO DE APLICACIÓN`,
    `==================`,
    `${t}`,
    ``,
    `INFORMACIÓN DEL LEAD`,
    `====================`,
    `Nombre: ${body.name}`,
    `Email: ${body.email}`,
    `Teléfono: ${body.phone}`,
    `Marca: ${body.brand}`,
    `URL / Instagram: ${body.website || '—'}`,
  ];
  if (body.applyType === 'partner') {
    lines.push(
      ``,
      `CALIFICACIÓN`,
      `============`,
      `Categoría: ${body.category || '—'}`,
      `Tiempo vendiendo online: ${body.time_selling || '—'}`,
      `Facturación mensual: ${body.revenue || '—'}`,
      `Inversión mensual en pauta: ${body.ad_spend || '—'}`,
      `Trabaja con agencia hoy: ${body.has_agency || '—'}`,
    );
  } else {
    lines.push(
      ``,
      `CALIFICACIÓN`,
      `============`,
      `Etapa: ${body.stage || '—'}`,
      `Qué vende: ${body.what_you_sell || '—'}`,
      `Facturación mensual: ${body.revenue || '—'}`,
      `Qué ha probado: ${body.tried || '—'}`,
    );
  }
  lines.push(
    ``,
    `OBJETIVO / QUÉ QUIERE RESOLVER`,
    `==============================`,
    body.goal || '—',
    ``,
    `ENLACE DE VIDEOLLAMADA`,
    `======================`,
    CONFIG.meetLink,
  );
  return lines.join('\n');
}

function rowForSheets(body, date, time, timestamp) {
  // Columns A..R = 18 columns. Single sheet stores both partner & advisor leads;
  // some columns may be empty depending on the type.
  const formattedDate = new Date(`${date}T${time}:00-05:00`).toLocaleDateString('es-CO', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
  });
  return [
    timestamp,                              // A — Timestamp ISO
    body.applyType === 'advisor' ? 'Advisor' : 'Partner', // B — Tipo
    body.name || '',                        // C
    body.email || '',                       // D
    body.phone || '',                       // E
    body.brand || '',                       // F
    body.website || '',                     // G
    body.category || '',                    // H — only partner
    body.time_selling || '',                // I — only partner
    body.revenue || '',                     // J — both
    body.ad_spend || '',                    // K — only partner
    body.has_agency || '',                  // L — only partner
    body.stage || '',                       // M — only advisor
    body.what_you_sell || '',               // N — only advisor
    body.tried || '',                       // O — only advisor
    body.goal || '',                        // P — both
    formattedDate,                          // Q — fecha legible
    time,                                   // R — hora
  ];
}

module.exports = async (req, res) => {
  // CORS preflight
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const body = req.body || {};
    const applyType = body.applyType === 'advisor' ? 'advisor' : 'partner';
    const { date, time } = body;

    // Validate required fields
    const required = [...REQUIRED[applyType], 'date', 'time'];
    const missing = required.filter((k) => !body[k] || String(body[k]).trim() === '');
    if (missing.length > 0) {
      return res.status(400).json({ error: 'Missing required fields', missing });
    }

    // Dev fallback — no Google creds yet
    if (!process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL || !process.env.GOOGLE_PRIVATE_KEY) {
      return res.status(200).json({
        success: true,
        mode: 'development',
        eventId: 'dev-' + Date.now(),
        meetLink: CONFIG.meetLink,
        date, time, applyType,
        message: 'Booking simulated (no Google credentials configured)',
      });
    }

    const { calendar, sheets } = getClients();
    const calendarId = process.env.GOOGLE_CALENDAR_ID;

    // ISO with Colombia offset (UTC-5)
    const startISO = `${date}T${time}:00-05:00`;
    const startDate = new Date(startISO);
    const endDate = new Date(startDate.getTime() + CONFIG.slotDuration * 60 * 1000);

    const event = {
      summary: `LA REAL · ${applyType === 'advisor' ? 'Advisor' : 'Partner'} — ${body.name} (${body.brand})`,
      description: buildDescription(body),
      start: { dateTime: startDate.toISOString(), timeZone: CONFIG.timezone },
      end:   { dateTime: endDate.toISOString(),   timeZone: CONFIG.timezone },
    };

    const calendarResponse = await calendar.events.insert({
      calendarId,
      resource: event,
    });

    // Append to Google Sheets (optional)
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
        // Do not fail the booking if Sheets fails
      }
    }

    return res.status(200).json({
      success: true,
      eventId: calendarResponse.data.id,
      meetLink: CONFIG.meetLink,
      date, time, applyType,
    });
  } catch (err) {
    console.error('book-appointment error:', err);
    return res.status(500).json({ error: err.message || 'Internal error' });
  }
};
