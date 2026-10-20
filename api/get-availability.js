// LA REAL — horarios disponibles para un día, cruzando los calendarios de Juanfe
const { isMockMode, hasCredentials, getClients, isBookableDate, allSlots, busyPeriods, freeSlots } = require('./_calendar');

module.exports = async (req, res) => {
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  const { date } = req.query;
  if (!date) return res.status(400).json({ error: 'Date parameter is required' });
  if (!isBookableDate(date)) return res.status(200).json({ date, available_slots: [] });

  try {
    if (isMockMode()) {
      // Solo en local / previews sin credenciales
      return res.status(200).json({ date, available_slots: freeSlots(date, []).filter((_, i) => i % 3 !== 1), mode: 'development' });
    }
    if (!hasCredentials()) return res.status(503).json({ error: 'Agenda no configurada' });

    const { calendar } = getClients();
    const busy = await busyPeriods(calendar, date);
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({ date, available_slots: freeSlots(date, busy), total_slots: allSlots().length });
  } catch (error) {
    console.error('Error getting availability:', error);
    return res.status(500).json({ error: 'Error getting availability' });
  }
};
