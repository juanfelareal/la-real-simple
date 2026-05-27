const { google } = require('googleapis');

// Configuración de disponibilidad
const CONFIG = {
    startHour: 9,        // 9 AM
    endHour: 17,         // 5 PM
    slotDuration: 30,    // minutos
    bufferTime: 15,      // minutos entre citas
    workDays: [1, 2, 3, 4, 5], // Lunes a Viernes
    timezone: 'America/Bogota'
};

// Inicializar cliente de Google Calendar
function getCalendarClient() {
    const auth = new google.auth.GoogleAuth({
        credentials: {
            client_email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
            private_key: process.env.GOOGLE_PRIVATE_KEY?.replace(/\\n/g, '\n')
        },
        scopes: ['https://www.googleapis.com/auth/calendar.readonly']
    });

    return google.calendar({ version: 'v3', auth });
}

// Generar todos los slots posibles para un día
function generateTimeSlots(date) {
    const slots = [];
    const startMinutes = CONFIG.startHour * 60;
    const endMinutes = CONFIG.endHour * 60;

    for (let minutes = startMinutes; minutes < endMinutes; minutes += CONFIG.slotDuration + CONFIG.bufferTime) {
        const hours = Math.floor(minutes / 60);
        const mins = minutes % 60;
        slots.push(`${hours.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}`);
    }

    return slots;
}

// Verificar si un slot está disponible
function isSlotAvailable(slotTime, busyPeriods, date) {
    const [hours, minutes] = slotTime.split(':').map(Number);
    const slotStart = new Date(date);
    slotStart.setHours(hours, minutes, 0, 0);

    const slotEnd = new Date(slotStart);
    slotEnd.setMinutes(slotEnd.getMinutes() + CONFIG.slotDuration);

    // Verificar contra cada período ocupado
    for (const busy of busyPeriods) {
        const busyStart = new Date(busy.start);
        const busyEnd = new Date(busy.end);

        // Si hay superposición, el slot no está disponible
        if (slotStart < busyEnd && slotEnd > busyStart) {
            return false;
        }
    }

    return true;
}

module.exports = async (req, res) => {
    // Manejar CORS preflight
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    try {
        const { date } = req.query;

        if (!date) {
            return res.status(400).json({ error: 'Date parameter is required' });
        }

        // Parsear la fecha
        const requestedDate = new Date(date + 'T00:00:00');
        const dayOfWeek = requestedDate.getDay();

        // Convertir domingo (0) a 7 para facilitar comparación
        const dayIndex = dayOfWeek === 0 ? 7 : dayOfWeek;

        // Verificar si es día laboral
        if (!CONFIG.workDays.includes(dayIndex)) {
            return res.status(200).json({
                date,
                available_slots: [],
                message: 'Not a working day'
            });
        }

        // Verificar si las credenciales están configuradas
        if (!process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL || !process.env.GOOGLE_PRIVATE_KEY) {
            // Modo de desarrollo: devolver slots simulados
            console.log('Running in development mode - returning mock slots');
            const allSlots = generateTimeSlots(requestedDate);

            // Simular algunos slots ocupados aleatoriamente
            const availableSlots = allSlots.filter(() => Math.random() > 0.3);

            return res.status(200).json({
                date,
                available_slots: availableSlots,
                mode: 'development'
            });
        }

        const calendar = getCalendarClient();
        const calendarId = process.env.GOOGLE_CALENDAR_ID;

        // Definir el rango de tiempo para consultar
        const timeMin = new Date(date + 'T00:00:00-05:00'); // Inicio del día en hora Colombia
        const timeMax = new Date(date + 'T23:59:59-05:00'); // Fin del día

        // Obtener eventos ocupados
        const freeBusyResponse = await calendar.freebusy.query({
            requestBody: {
                timeMin: timeMin.toISOString(),
                timeMax: timeMax.toISOString(),
                timeZone: CONFIG.timezone,
                items: [{ id: calendarId }]
            }
        });

        const busyPeriods = freeBusyResponse.data.calendars[calendarId]?.busy || [];

        // Generar todos los slots posibles
        const allSlots = generateTimeSlots(requestedDate);

        // Filtrar slots disponibles
        const availableSlots = allSlots.filter(slot =>
            isSlotAvailable(slot, busyPeriods, date)
        );

        // Filtrar slots que ya pasaron (si es hoy)
        const now = new Date();
        const today = now.toISOString().split('T')[0];

        let finalSlots = availableSlots;
        if (date === today) {
            const currentHour = now.getHours();
            const currentMinutes = now.getMinutes();
            const currentTotalMinutes = currentHour * 60 + currentMinutes;

            // Agregar buffer de 2 horas para citas del mismo día
            const minBookingMinutes = currentTotalMinutes + 120;

            finalSlots = availableSlots.filter(slot => {
                const [h, m] = slot.split(':').map(Number);
                return (h * 60 + m) >= minBookingMinutes;
            });
        }

        return res.status(200).json({
            date,
            available_slots: finalSlots
        });

    } catch (error) {
        console.error('Error getting availability:', error);
        return res.status(500).json({
            error: 'Error getting availability',
            details: error.message
        });
    }
};
