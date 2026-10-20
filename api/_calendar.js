// LA REAL — helpers compartidos de agenda (no es una ruta: Vercel ignora archivos con "_")
// Los horarios se calculan siempre en hora de Bogotá (UTC-5, sin horario de verano),
// sin importar la zona horaria del servidor.

const { google } = require('googleapis');

const CONFIG = {
  startHour: 10,         // ninguna llamada empieza antes de las 10 AM
  endHour: 17,           // y todas terminan a más tardar a las 5 PM
  slotDuration: 30,      // minutos
  bufferTime: 15,        // minutos entre citas
  workDays: [1, 2, 3, 4, 5], // lunes a viernes
  minNoticeMinutes: 120, // no se agenda con menos de 2 horas
  maxDaysAhead: 30,
  timezone: 'America/Bogota',
  offset: '-05:00',
  meetLink: 'https://meet.google.com/jqb-ryky-kqx',
};

// Calendarios donde se revisa disponibilidad (los dos de Juanfe)
function busyCalendarIds() {
  const raw = process.env.GOOGLE_CALENDAR_IDS || process.env.GOOGLE_CALENDAR_ID
    || 'juanfe@larealmarketing.com,juanfelipeleonleon@gmail.com';
  return raw.split(',').map((s) => s.trim()).filter(Boolean);
}

// Calendarios donde se crea la cita. Por defecto solo el de LA REAL: la cuenta de Gmail
// ya lo ve compartido, así que crearla en ambos la duplicaría. Si la cuenta de servicio
// no tiene permiso de escritura en alguno, se omite y se registra en el log.
function eventCalendarIds() {
  const raw = process.env.GOOGLE_EVENT_CALENDAR_IDS || 'juanfe@larealmarketing.com';
  return raw.split(',').map((s) => s.trim()).filter(Boolean);
}

function hasCredentials() {
  return Boolean(process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL && process.env.GOOGLE_PRIVATE_KEY);
}

// En producción nunca se simulan horarios: sin credenciales, la agenda responde error
function isMockMode() {
  return !hasCredentials() && process.env.VERCEL_ENV !== 'production';
}

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

function slotStart(date, time) {
  return new Date(`${date}T${time}:00${CONFIG.offset}`);
}

function bogotaToday() {
  return new Date(Date.now() - 5 * 3600 * 1000).toISOString().slice(0, 10);
}

function isWorkDay(date) {
  const dow = new Date(`${date}T12:00:00${CONFIG.offset}`).getUTCDay();
  return CONFIG.workDays.includes(dow === 0 ? 7 : dow);
}

function isBookableDate(date) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return false;
  const days = (new Date(`${date}T00:00:00Z`) - new Date(`${bogotaToday()}T00:00:00Z`)) / 86400000;
  return days >= 0 && days <= CONFIG.maxDaysAhead && isWorkDay(date);
}

function allSlots() {
  const slots = [];
  for (let m = CONFIG.startHour * 60; m + CONFIG.slotDuration <= CONFIG.endHour * 60; m += CONFIG.slotDuration + CONFIG.bufferTime) {
    slots.push(`${String(Math.floor(m / 60)).padStart(2, '0')}:${String(m % 60).padStart(2, '0')}`);
  }
  return slots;
}

// Períodos ocupados sumando todos los calendarios
async function busyPeriods(calendar, date) {
  const ids = busyCalendarIds();
  const res = await calendar.freebusy.query({
    requestBody: {
      timeMin: new Date(`${date}T00:00:00${CONFIG.offset}`).toISOString(),
      timeMax: new Date(`${date}T23:59:59${CONFIG.offset}`).toISOString(),
      timeZone: CONFIG.timezone,
      items: ids.map((id) => ({ id })),
    },
  });
  const busy = [];
  for (const id of ids) {
    const c = res.data.calendars?.[id];
    if (c?.errors?.length) console.error(`freebusy sin acceso a ${id}:`, c.errors);
    busy.push(...(c?.busy || []));
  }
  return busy;
}

function freeSlots(date, busy) {
  const earliest = Date.now() + CONFIG.minNoticeMinutes * 60000;
  return allSlots().filter((t) => {
    const start = slotStart(date, t);
    const end = new Date(start.getTime() + CONFIG.slotDuration * 60000);
    if (start.getTime() < earliest) return false;
    return !busy.some((b) => start < new Date(b.end) && end > new Date(b.start));
  });
}

module.exports = {
  CONFIG, busyCalendarIds, eventCalendarIds, hasCredentials, isMockMode, getClients,
  slotStart, isBookableDate, allSlots, busyPeriods, freeSlots,
};
