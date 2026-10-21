// Exporta cada .slide de disenos.html a ../assets/carrusel-<id>.jpg (1600×1600).
// Uso: node bloki-preview/carrusel/render.js
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1600 } });
  await page.goto('file://' + path.join(__dirname, 'disenos.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const el of await page.$$('.slide')) {
    const id = await el.getAttribute('id');
    const out = path.join(__dirname, '..', 'assets', `carrusel-${id}.jpg`);
    await el.screenshot({ path: out, type: 'jpeg', quality: 88 });
    console.log(out);
  }
  await browser.close();
})();
