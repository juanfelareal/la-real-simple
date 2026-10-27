// Exporta cada .ig de posts.html a instagram/export/<id>.jpg
// Uso: node bloki-preview/instagram/render-ig.js
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const out = path.join(__dirname, 'export');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(__dirname, 'posts.html'));
  await page.evaluate(() => document.fonts.ready);
  for (const el of await page.$$('.ig')) {
    const id = await el.getAttribute('id');
    const file = path.join(out, `${id}.jpg`);
    await el.screenshot({ path: file, type: 'jpeg', quality: 92 });
    console.log(file);
  }
  await browser.close();
})();
