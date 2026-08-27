/**
 * INSTRUCCIONES DE CONFIGURACIÓN:
 *
 * 1. Ve a https://script.google.com y crea un nuevo proyecto
 * 2. Copia todo este código y pégalo en el editor
 * 3. Crea una hoja de Google Sheets llamada "LA REAL - Leads Diagnósticos"
 * 4. Copia el ID de la hoja (está en la URL: docs.google.com/spreadsheets/d/{ESTE_ES_EL_ID}/edit)
 * 5. Pega el ID abajo en SPREADSHEET_ID
 * 6. Guarda el proyecto (Ctrl+S)
 * 7. Click en "Implementar" > "Nueva implementación"
 * 8. Selecciona tipo: "Aplicación web"
 * 9. Ejecutar como: "Yo"
 * 10. Quién tiene acceso: "Cualquier persona"
 * 11. Click en "Implementar" y copia la URL del web app
 * 12. Esa URL es la que va en WEBHOOK_URL en los diagnósticos HTML
 *
 * La hoja de cálculo creará automáticamente los headers en la primera fila.
 */

// ===== CONFIGURACIÓN =====
const SPREADSHEET_ID = 'TU_SPREADSHEET_ID_AQUI'; // Reemplaza con el ID de tu hoja
const NOTIFICATION_EMAIL = 'juanfe@larealmarketing.com';
const SHEET_NAME = 'Leads'; // Nombre de la pestaña

// ===== NO MODIFICAR ABAJO =====

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    // Abrir la hoja
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    let sheet = ss.getSheetByName(SHEET_NAME);

    // Si no existe la hoja, crearla con headers
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow([
        'Fecha',
        'Hora',
        'Diagnóstico',
        'Nombre',
        'Marca',
        'WhatsApp',
        'Email',
        'URL Tienda',
        'Ventas Mensuales',
        'Puntaje',
        'Nivel',
        'Plan Recomendado'
      ]);
      // Formato de headers
      sheet.getRange(1, 1, 1, 12).setFontWeight('bold').setBackground('#f0f0f0');
    }

    // Formatear fecha y hora Colombia (UTC-5)
    const now = new Date();
    const colombiaTime = new Date(now.getTime() - (5 * 60 * 60 * 1000));
    const fecha = Utilities.formatDate(colombiaTime, 'America/Bogota', 'yyyy-MM-dd');
    const hora = Utilities.formatDate(colombiaTime, 'America/Bogota', 'HH:mm:ss');

    // Agregar fila con los datos
    sheet.appendRow([
      fecha,
      hora,
      data.diagnostico || '',
      data.nombre || '',
      data.marca || '',
      data.whatsapp || '',
      data.email || '',
      data.url || '',
      data.ventas || '',
      data.puntaje || '',
      data.nivel || '',
      data.plan || ''
    ]);

    // Enviar notificación por email
    sendNotificationEmail(data, fecha, hora);

    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function sendNotificationEmail(data, fecha, hora) {
  const diagnosticoNames = {
    'email': 'Email Marketing',
    'ugc': 'UGC / Contenido',
    'shopify': 'Shopify'
  };

  const diagName = diagnosticoNames[data.diagnostico] || data.diagnostico;

  const subject = `🔔 Nuevo lead: ${data.marca} — Diagnóstico ${diagName}`;

  const body = `
¡Nuevo lead desde el diagnóstico de ${diagName}!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 DATOS DEL LEAD

• Nombre: ${data.nombre}
• Marca: ${data.marca}
• WhatsApp: ${data.whatsapp}
• Email: ${data.email}
• URL Tienda: ${data.url || 'No proporcionada'}
• Ventas mensuales: ${data.ventas}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 RESULTADO DEL DIAGNÓSTICO

• Puntaje: ${data.puntaje}/100
• Nivel: ${data.nivel}
• Plan recomendado: ${data.plan}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🕐 Registrado: ${fecha} a las ${hora} (Colombia)

👉 Contactar por WhatsApp: https://wa.me/${data.whatsapp.replace(/\D/g, '')}

—
LA REAL · Sistema de Diagnósticos
`;

  MailApp.sendEmail({
    to: NOTIFICATION_EMAIL,
    subject: subject,
    body: body
  });
}

// Test function (para probar en el editor)
function testDoPost() {
  const testData = {
    postData: {
      contents: JSON.stringify({
        diagnostico: 'email',
        nombre: 'Test Usuario',
        marca: 'Test Marca',
        whatsapp: '+573001234567',
        email: 'test@test.com',
        url: 'www.testmarca.com',
        ventas: '$10M – $30M',
        puntaje: 65,
        nivel: 'Transición',
        plan: 'Email Automation Pro'
      })
    }
  };

  const result = doPost(testData);
  Logger.log(result.getContent());
}
