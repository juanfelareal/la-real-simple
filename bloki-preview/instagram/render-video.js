// Genera export/p3-1-animada.mp4 a partir de portada-animada.html, cuadro por cuadro (30 fps).
// Uso: node bloki-preview/instagram/render-video.js <carpeta-temporal>
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

const FPS = 30, ANIM_MS = 3200, HOLD_MS = 3000, LEAD_MS = 400;

(async () => {
  const tmp = process.argv[2];
  fs.mkdirSync(tmp, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto('file://' + path.join(__dirname, 'portada-animada.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => {
    document.body.classList.add('go');
    document.getAnimations().forEach(a => a.pause());
  });
  const total = Math.round((LEAD_MS + ANIM_MS + HOLD_MS) / 1000 * FPS);
  for (let i = 0; i < total; i++) {
    const t = Math.max(0, i * 1000 / FPS - LEAD_MS);
    await page.evaluate(ms => document.getAnimations().forEach(a => { a.currentTime = ms; }), t);
    await page.screenshot({ path: path.join(tmp, `f${String(i).padStart(4, '0')}.png`) });
  }
  await browser.close();
  const out = path.join(__dirname, 'export', 'p3-1-animada.mp4');
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', String(FPS), '-i', path.join(tmp, 'f%04d.png'),
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]);
  console.log(out);
})();
