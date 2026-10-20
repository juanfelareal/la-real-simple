#!/usr/bin/env python3
"""Genera las páginas de servicio en servicios/*.html.

Las tarjetas de precios se copian tal cual desde index.html (por su data-book),
así un cambio de precio en la home se refleja aquí al volver a correr:
    python3 scripts/servicios.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = (ROOT / 'index.html').read_text()
OUT = ROOT / 'servicios'

PIXEL = HOME[HOME.index('<!-- Meta Pixel Code -->'):HOME.index('<!-- End Meta Pixel Code -->') + len('<!-- End Meta Pixel Code -->')]


def price_card(service):
    """La tarjeta <article> de la home cuyo botón agenda este servicio, con rutas ajustadas."""
    for m in re.finditer(r'<article class="svc[^"]*">.*?</article>', HOME, flags=re.S):
        if f'data-book="{service}"' in m.group(0):
            card = m.group(0).replace(' rv"', '"')
            return re.sub(r'<a class="svc-more"[^>]*>.*?</a>', '', card)
    raise SystemExit(f'No encontré la tarjeta de precios de {service} en index.html')


def cards(items, cls=''):
    return f'<div class="sp-cards {cls}">' + ''.join(
        f'<div class="sp-card rv"><span class="k">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(items)) + '</div>'


def bullets(items):
    return '<ul class="sp-list">' + ''.join(
        f'<li class="rv"><div>{t}{f"<span>{d}</span>" if d else ""}</div></li>' for t, d in items) + '</ul>'


def faq(items):
    return '<div class="faq">' + ''.join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'


def section(label, title, body, intro='', sid=''):
    intro_html = f'<p class="sp-intro rv">{intro}</p>' if intro else ''
    return f'''
  <section class="sp-sec"{f' id="{sid}"' if sid else ''}>
    <div class="wrap">
      <p class="label rv">{label}</p>
      <h2 class="h2 rv">{title}</h2>
      {intro_html}
      {body}
    </div>
  </section>'''


def page(s):
    svc = s['service']
    pills = ''.join(f'<p class="scope">{p}</p>' for p in s.get('pills', []))
    body = ''.join(section(*sec) if isinstance(sec, tuple) else sec for sec in s['sections'])
    work_link = ('<a href="#trabajo">Trabajo</a>' if 'id="trabajo"' in body
                 else '<a href="#orbit">Orbit</a>' if 'id="orbit"' in body else '')
    return f'''<!doctype html>
<html lang="es">
<head>
{PIXEL}
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<title>{s['title']} · LA REAL</title>
<meta name="description" content="{s['meta']}" />
<meta name="theme-color" content="#F3F1ED" />
<meta property="og:title" content="{s['title']} · LA REAL" />
<meta property="og:description" content="{s['meta']}" />
<meta property="og:image" content="https://landing.larealmarketing.com/assets/icon-192.png" />
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="../assets/apple-touch-icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="../assets/lr-min.css" />
<link rel="stylesheet" href="../assets/agenda.css" />
</head>
<body>

<header class="nav" id="nav">
  <div class="wrap">
    <a href="../" class="brand"><img src="../assets/brand/iso-navy-sm.png" alt="">LA REAL</a>
    <nav class="nav-links">
      <a href="#incluye">Qué incluye</a>
      {work_link}
      <a href="#precios">Precios</a>
    </nav>
    <button class="btn btn-dark" data-book="{svc}">Agendar llamada</button>
  </div>
</header>

<main>
  <section class="sp-hero">
    <div class="wrap">
      <a class="sp-back" href="../#servicios">← Todos los servicios</a>
      <p class="label hero-label"><span class="dot"></span>Servicio {s['num']} · {svc}</p>
      <h1 class="h1">{s['h1']}</h1>
      <p class="lead">{s['lead']}</p>
      <div class="sp-pills">{pills}</div>
      <div class="hero-ctas">
        <button class="btn btn-dark" data-book="{svc}">Agendar llamada</button>
        <a class="btn btn-ghost" href="#precios">Ver precios</a>
      </div>
    </div>
  </section>
{body}
  <section class="sp-sec" id="precios">
    <div class="wrap">
      <p class="label rv">Precios</p>
      <h2 class="h2 rv">Lo que cuesta, <b>sin letra pequeña.</b></h2>
      <div class="sp-price">{price_card(svc)}</div>
    </div>
  </section>

  <section class="sp-sec">
    <div class="wrap">
      <p class="label rv">Preguntas frecuentes</p>
      {faq(s['faq'])}
    </div>
  </section>

  <section class="closing">
    <div class="wrap">
      <div class="who"><img src="../assets/team/juanfe-sm.jpg" alt="">Te atiende Juanfe<span class="dot"></span></div>
      <h2 class="h2"><b>Hablemos de tu marca.</b><br><span class="soft">30 minutos, por videollamada.</span></h2>
      <p>Revisamos tus números y te decimos si este servicio es lo que tu marca necesita ahora.</p>
      <div class="closing-ctas"><button class="btn btn-light" data-book="{svc}">Agendar llamada</button></div>
      <small>Medellín · Trabajamos con marcas en todo el mundo</small>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <span>© 2026 LA REAL Marketing</span>
    <nav>
      <a href="../">Inicio</a>
      <a href="https://instagram.com/larealmarketing" target="_blank" rel="noopener">Instagram</a>
      <a href="mailto:juanfe@larealmarketing.com">Correo</a>
      <a href="../assets/politica-datos.pdf" target="_blank" rel="noopener">Política de datos</a>
    </nav>
  </div>
</footer>

<script>
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 8);
addEventListener('scroll', onScroll, {{passive:true}}); onScroll();

const io = new IntersectionObserver(es => es.forEach(e => {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}), {{rootMargin:'0px 0px -8% 0px'}});
document.querySelectorAll('.rv').forEach(el => io.observe(el));

// Flechas para las filas deslizables (en computador no siempre hay trackpad)
document.querySelectorAll('.sp-row').forEach(row => {{
  const nav = document.createElement('div'); nav.className = 'sp-nav';
  nav.innerHTML = '<button type="button" aria-label="Anterior">←</button><button type="button" aria-label="Siguiente">→</button>';
  row.after(nav);
  const [prev, next] = nav.querySelectorAll('button');
  const sync = () => {{ prev.disabled = row.scrollLeft < 4; next.disabled = row.scrollLeft + row.clientWidth >= row.scrollWidth - 4; nav.hidden = row.scrollWidth <= row.clientWidth + 4; }};
  prev.onclick = () => row.scrollBy({{left: -row.clientWidth * .8, behavior: 'smooth'}});
  next.onclick = () => row.scrollBy({{left: row.clientWidth * .8, behavior: 'smooth'}});
  row.addEventListener('scroll', sync, {{passive:true}}); addEventListener('resize', sync); sync();
}});

// Videos: se reproducen en silencio al verse; el botón activa el sonido
const vio = new IntersectionObserver(es => es.forEach(e => e.isIntersecting ? e.target.play().catch(() => {{}}) : e.target.pause()), {{threshold:.6}});
document.querySelectorAll('.sp-vid video').forEach(v => vio.observe(v));
document.querySelectorAll('.sp-vid button').forEach(b => b.addEventListener('click', () => {{
  const v = b.previousElementSibling; v.muted = !v.muted; b.textContent = v.muted ? 'Activar sonido' : 'Silenciar';
  if (!v.muted) document.querySelectorAll('.sp-vid video').forEach(o => {{ if (o !== v) {{ o.muted = true; o.nextElementSibling.textContent = 'Activar sonido'; }} }});
}}));
</script>
<script>
// Orbit (vista de ejemplo): el contador vuelve a 0 cada 3 minutos, como la sincronización real
const om = document.getElementById('orbit-min');
if (om) {{ let t = 2; setInterval(() => {{ t = (t + 1) % 3; om.textContent = t; }}, 60000); }}
</script>
<script src="../assets/agenda.js" defer></script>
</body>
</html>
'''


A = '../assets/servicios'

# ---------- Galerías ----------
CASES = [
    ('dulcey', 'Dulcey', 'calzadodulcey.com', 'Rediseño editorial para una marca de calzado en cuero hecho a mano, con la sobriedad de las casas europeas de lujo.', ['Rediseño', 'Shopify 2.0', 'Secciones a la medida']),
    ('gratu', 'Gratu', 'gratu.co', 'Páginas de producto para planeadores y cuadernos, con packs nativos en lugar de apps de terceros.', ['Fichas de producto', 'Packs y descuentos']),
    ('estruendo', 'Estruendo', 'estruendohacemos.co', 'Optimización de la tienda y una landing de los más vendidos para llevar la pauta a los productos que más venden.', ['Optimización', 'Landing de campaña']),
    ('atratus', 'Atratus', 'atratuscolombia.com', 'De una plantilla genérica en Wix a una tienda propia en Shopify, a la altura de una marca de ropa outdoor colombiana.', ['Migración desde Wix', 'Diseño a la medida']),
    ('natnack', 'Natnack', 'natnack.com', 'Optimización de la tienda de snacks de legumbres para que la marca y el producto se entiendan desde el primer segundo.', ['Optimización', 'Conversión']),
]


def case(i, k, name, url, desc, tags):
    extra = ''
    if k == 'atratus':
        extra = f'''
          <div class="sp-ba">
            <figure><img src="{A}/shopify/atratus-antes.jpg" alt="Sitio de Atratus antes, en Wix" loading="lazy"><figcaption>Antes · Wix</figcaption></figure>
            <figure><img src="{A}/shopify/atratus-despues.jpg" alt="Sitio de Atratus después, en Shopify" loading="lazy"><figcaption>Después · Shopify</figcaption></figure>
          </div>'''
    return f'''
        <article class="case rv">
          <div class="case-stage">
            <div class="browser"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><img src="{A}/shopify/{k}-pc.jpg" alt="Sitio de {name} en computador" loading="lazy"></div>
            <div class="phone"><img src="{A}/shopify/{k}-movil.jpg" alt="Sitio de {name} en celular" loading="lazy"></div>
          </div>
          <div class="case-info">
            <span class="k">{i:02d}</span>
            <div><h3>{name}</h3><p>{desc}</p><div class="case-tags">{''.join(f'<span>{t}</span>' for t in tags)}</div></div>
            <a class="case-link" href="https://{url}" target="_blank" rel="noopener">Visitar sitio ↗</a>
          </div>{extra}
        </article>'''


cases_html = '<div class="cases">' + ''.join(case(i + 1, *c) for i, c in enumerate(CASES)) + '</div>'

ORBIT = '''
  <section class="orbit" id="orbit">
    <div class="wrap">
      <div class="orbit-copy">
        <p class="label rv">Orbit · dashboard en vivo</p>
        <h2 class="h2 rv"><b>Tus números en tiempo real.</b> <span class="soft">No esperas al reporte.</span></h2>
        <p class="rv">Cada cliente tiene acceso a Orbit, nuestro dashboard. Los datos de tu tienda y de tu pauta se actualizan solos cada 3 minutos, sin hojas de cálculo ni capturas de pantalla.</p>
        <ul class="orbit-points rv">
          <li>Ventas, pedidos y ticket promedio de Shopify</li>
          <li>Inversión y retorno de Meta, cruzados con tu venta real</li>
          <li>Comparación contra el mes anterior y tus objetivos</li>
          <li>Desde el computador o el celular, cuando quieras</li>
        </ul>
      </div>
      <div class="rv">
        <div class="dash" aria-label="Vista de ejemplo del dashboard Orbit">
          <div class="dash-head"><div><b>Orbit</b><small>Tu marca · este mes</small></div><span class="live"><i></i>Actualizado hace <span id="orbit-min">2</span> min</span></div>
          <div class="dash-kpis">
            <div class="kpi"><small>Venta neta</small><b>$84,2M</b><em>↑ 12% vs mes ant.</em></div>
            <div class="kpi"><small>Pedidos</small><b>612</b><em>↑ 9%</em></div>
            <div class="kpi"><small>Inversión Meta</small><b>$18,6M</b><em>22% de la venta</em></div>
            <div class="kpi"><small>Retorno</small><b>4,5x</b><em>sobre venta neta</em></div>
          </div>
          <div class="dash-chart"><div class="t"><span>Venta neta por día</span><span>■ Shopify &nbsp;<span style="color:#B5B1AA">■</span> Inversión</span></div>
            <div class="bars">{bars}</div></div>
        </div>
        <p class="dash-note">Vista de ejemplo con datos ilustrativos.</p>
      </div>
    </div>
  </section>'''.replace('{bars}', ''.join(f'<span style="height:{h}%"></span><span class="m" style="height:{m}%"></span>' for h, m in [(48,14),(62,15),(55,13),(70,16),(66,15),(82,18),(74,17),(90,19),(78,18),(95,20)]))

VIDEOS = [
    ('si-sammy', 'Sin Intermediarios'), ('adriza-berberina', 'Adriza'), ('A1_acrilico-no-se-acaba', 'Gratu'),
    ('si-yeyo', 'Sin Intermediarios'), ('adriza-magnesio', 'Adriza'),
    ('C5_cosido-antes-despues', 'Gratu'), ('si-natalia', 'Sin Intermediarios'), ('adriza-ashwagandha', 'Adriza'),
    ('si-gabriela', 'Sin Intermediarios'),
]


def video(v, brand):
    return f'''
        <div class="sp-vid"><video src="{A}/ugc/{v}.mp4" poster="{A}/ugc/{v}.jpg" muted loop playsinline preload="none"></video><button type="button">Activar sonido</button></div>'''


videos_html = '<div class="sp-row">' + ''.join(video(*v) for v in VIDEOS) + '</div>'

EMAILS = ['guuut', 'moi-a', 'dulcey-campana', 'natnack', 'atratus-bienvenida', 'moi-d', 'bites', 'adriza',
          'zorro-jaguar', 'estruendo', 'moi-c', 'gratu', 'dulcey-padre', 'adriza-pack', 'atratus-padres']
emails_html = '<div class="sp-row">' + ''.join(f'''
        <div class="sp-mail"><div class="scroll"><img src="{A}/email/{k}.jpg" alt="Correo de email marketing" loading="lazy"></div></div>''' for k in EMAILS) + '</div>'

# ---------- Contenido ----------
SERVICES = {
    'shopify': {
        'service': 'Sitio web en Shopify', 'num': '01', 'title': 'Sitio web en Shopify',
        'meta': 'Diseñamos, construimos y optimizamos tiendas en Shopify para marcas de ecommerce.',
        'h1': 'Una tienda a la altura de tu marca, <b>hecha para vender.</b>',
        'lead': 'Diseñamos, construimos y optimizamos tiendas en Shopify. Partimos de cómo compra tu cliente y de los datos de tu tienda actual, no de una plantilla.',
        'pills': ['Hasta 50 productos · un idioma · un mercado'],
        'sections': [
            ('Para quién es', 'Si te identificas con algo de esto, <b>hablemos.</b>',
             cards([('Vendes en otra plataforma', 'Estás en Wix, WooCommerce u otra plataforma y quieres pasarte a Shopify sin perder ventas.'),
                    ('Tu tienda no se ve como tu marca', 'El producto es bueno, pero la tienda parece una plantilla más.'),
                    ('Te visitan y no compran', 'Tienes tráfico, pero la conversión no acompaña la inversión en pauta.')])),
            ('Qué incluye', 'Todo lo que necesita <b>una tienda que vende.</b>',
             bullets([('Diagnóstico de tu tienda actual', 'Analítica, recorrido de compra y referentes de tu categoría.'),
                      ('Arquitectura de la tienda', 'Menú, colecciones y fichas de producto pensadas para comprar.'),
                      ('Diseño a la medida', 'Sobre un tema de Shopify 2.0 que tu equipo puede editar sin programar.'),
                      ('Piezas gráficas incluidas', 'Diseñamos los banners, la iconografía y todas las piezas que la tienda necesita para convertir. Tú solo apruebas.'),
                      ('Celular primero', 'La mayoría de tus clientes compra desde el teléfono; ahí empezamos.'),
                      ('Migración', 'Productos, clientes y redirecciones para no perder posicionamiento.'),
                      ('Configuración de la operación', 'Pagos, envíos, impuestos y las apps que de verdad necesitas.'),
                      ('Velocidad y SEO técnico', 'Imágenes optimizadas, estructura limpia y metadatos.'),
                      ('Capacitación grabada', 'Para que tu equipo administre la tienda desde el primer día.')])
             + '<div class="sp-note rv"><b>Opcional · Optimización constante ($3.000.000 + IVA al mes):</b> si lo quieres, después del lanzamiento seguimos mejorando la tienda cada mes con base en sus datos: pruebas, landings de campaña y ajustes de conversión. No es obligatorio para hacer tu sitio.</div>',
             '', 'incluye'),
            ('Cómo trabajamos', 'Cuatro etapas, <b>en promedio 2 semanas.</b>',
             cards([('Diagnóstico', 'Revisamos tus números, tu tienda actual y lo que hace bien tu competencia.'),
                    ('Diseño', 'Te mostramos la propuesta en computador y celular, con banners e iconografía, antes de construir.'),
                    ('Construcción', 'Desarrollo, carga de productos, configuración y pruebas de compra.'),
                    ('Lanzamiento y seguimiento', 'Publicamos y revisamos el comportamiento de la tienda las semanas siguientes.')], 'c4')),
            ('Trabajo', 'Tiendas que <b>hemos hecho y optimizado.</b>', cases_html, 'Así se ven hoy, en computador y en celular.', 'trabajo'),
        ],
        'faq': [
            ('¿Mi equipo puede editar la tienda después?', 'Sí. Construimos sobre temas de Shopify 2.0 con secciones editables y te entregamos una capacitación grabada.'),
            ('¿Qué pasa si tengo más de 50 productos, varios idiomas o varios países?', 'Lo cotizamos según lo que necesites. El precio estándar cubre hasta 50 productos, un idioma y un mercado.'),
            ('¿La suscripción de Shopify y las apps están incluidas?', 'No. El plan de Shopify y las apps los pagas directamente a cada proveedor, a nombre de tu marca.'),
            ('¿Cuánto se demora?', 'El tiempo promedio de entrega es de 2 semanas. La fecha exacta queda en el contrato y, si nos atrasamos por causa nuestra, te devolvemos el 10% por cada semana.'),
            ('¿Tengo que entregar banners o diseños?', 'No. Nosotros diseñamos los banners, la iconografía y las piezas gráficas de la tienda. Tú solo apruebas.'),
            ('¿Qué diferencia hay entre rediseño y sitio desde cero?', 'En el rediseño partimos de tu tienda en Shopify y su contenido. Desde cero incluye montar la tienda completa o migrarla desde otra plataforma.'),
        ],
    },
    'pauta': {
        'service': 'Pauta para ecommerce', 'num': '02', 'title': 'Pauta para ecommerce',
        'meta': 'Gestión de pauta en Meta para ecommerce, medida contra tus ventas reales en Shopify.',
        'h1': 'Pauta en Meta <b>medida contra tus ventas reales.</b>',
        'lead': 'Gestionamos tus campañas con revisión diaria y reporte semanal. Medimos el retorno sobre tu venta neta en Shopify, no solo sobre lo que reporta Meta.',
        'pills': ['Incluye una plataforma: Meta', '15 piezas gráficas al mes', 'Desde $3M de inversión al mes'],
        'sections': [
            ('Para quién es', 'Para marcas que ya venden <b>y quieren crecer con rentabilidad.</b>',
             cards([('Inviertes y no sabes si es rentable', 'Meta dice una cosa, tu cuenta bancaria dice otra.'),
                    ('Tus anuncios se desgastaron', 'Lo que funcionaba hace tres meses ya no vende igual.'),
                    ('Quieres invertir más sin perder margen', 'Necesitas saber cuánto puedes subir la inversión y dónde.')])),
            ('Qué incluye', 'La gestión completa <b>de tu cuenta.</b>',
             bullets([('Auditoría de cuenta y medición', 'Píxel, API de conversiones y catálogo funcionando antes de invertir.'),
                      ('Estructura de campañas', 'Prospección, remarketing y catálogo, cada una con su objetivo.'),
                      ('Sistema de pruebas', 'Ángulos de venta cruzados con formatos: estático, video y UGC.'),
                      ('Revisión diaria', 'Presupuestos, anuncios y frecuencia, todos los días hábiles.'),
                      ('Dashboard en vivo en Orbit', 'Tus ventas y tu pauta actualizadas cada 3 minutos.'),
                      ('Reporte semanal', 'Qué pasó, qué cambiamos y por qué.'),
                      ('Reporte mensual en una página', 'Ventas, pauta, tienda y foco del siguiente mes. El análisis lo escribe el equipo.'),
                      ('15 piezas gráficas al mes', 'Diseñamos los anuncios gráficos de tus campañas según lo que está vendiendo. Tú solo apruebas.'),
                      ('Plataformas adicionales', 'Google o TikTok por $1.000.000 + IVA al mes cada una.')]),
             '', 'incluye'),
            ORBIT,
            ('Cómo trabajamos', 'Así decidimos <b>dónde va cada peso.</b>',
             cards([('Medimos', 'Conectamos la pauta con tus ventas en Shopify. El retorno se calcula sobre la venta neta.'),
                    ('Probamos', 'Lanzamos ángulos y formatos en conjuntos de prueba, con presupuesto controlado.'),
                    ('Escalamos', 'Elegimos ganadores por retorno y por volumen de ventas, no solo por retorno.'),
                    ('Revisamos', 'Cada semana ajustamos. Lo que funciona recibe más inversión; lo que no, se apaga.')], 'c4')),
        ],
        'faq': [
            ('¿La inversión en anuncios está incluida?', 'No. La inversión la pagas directamente a Meta con tu tarjeta. Nuestro valor es la gestión.'),
            ('¿Qué es el 4% de venta atribuida en Meta?', 'Aplica cuando inviertes más de $15M al mes: además del valor fijo, cobramos el 4% de las ventas que Meta atribuye a las campañas.'),
            ('¿Hay permanencia mínima?', 'No. Trabajamos mes a mes y las cuentas, audiencias y creativos son tuyos desde el primer día.'),
            ('¿Quién hace los creativos?', 'Las piezas gráficas las diseñamos nosotros: 15 al mes, incluidas en el servicio, y tú solo apruebas. Los videos con creadores los puede hacer tu equipo o nuestro servicio de contenido UGC.'),
            ('¿Manejan otras plataformas además de Meta?', 'Sí. Cada plataforma adicional, como Google o TikTok, cuesta $1.000.000 + IVA al mes.'),
        ],
    },
    'contenido-ugc': {
        'service': 'Estrategia y contenido UGC', 'num': '03', 'title': 'Estrategia y contenido UGC',
        'meta': 'Estrategia, creadores, guiones y análisis de videos UGC para pauta en ecommerce.',
        'h1': 'Contenido con creadores, <b>pensado para vender.</b>',
        'lead': 'No vendemos un paquete de videos. Armamos la estrategia, conseguimos los creadores, escribimos los guiones y medimos qué video vende para hacer más de esos.',
        'pills': ['Videos verticales listos para pauta', 'Con cesión de derechos'],
        'sections': [
            ('Para quién es', 'Para marcas que pautan y <b>necesitan creativos nuevos cada mes.</b>',
             cards([('Tus anuncios se cansan rápido', 'Necesitas material nuevo para que la pauta no se estanque.'),
                    ('No sabes qué contenido funciona', 'Has probado de todo, pero no sabes por qué un video vende y otro no.'),
                    ('Coordinar creadores te quita tiempo', 'Buscar, negociar, explicar y revisar es un trabajo completo.')])),
            ('Qué incluye', 'De la idea al video <b>y a la lectura de resultados.</b>',
             bullets([('Brief conjunto', 'Los ángulos de venta salen de tu cliente y de tus datos; no los inventamos antes.'),
                      ('Selección de creadores', 'Casting según tu cliente ideal, negociación y coordinación.'),
                      ('Guion y dirección creativa', 'Cada video con su gancho, su mensaje y su llamado a la acción.'),
                      ('Grabación y edición', 'Formato vertical, subtítulos y versiones listas para pauta.'),
                      ('Cesión de derechos', 'Para usar los videos en anuncios y en redes de tu marca.'),
                      ('Medición por video', 'Cada pieza etiquetada por ángulo, creador y formato.'),
                      ('Análisis mensual', 'Qué repetir, qué ajustar y qué cambiar en la siguiente tanda.')]),
             '', 'incluye'),
            ('Cómo trabajamos', 'Cinco pasos que <b>se repiten cada mes.</b>',
             cards([('Entender el negocio', 'Tu producto, tu cliente y lo que ya sabemos que vende.'),
                    ('Elegir creadores', 'Perfiles que se parecen a quien te compra.'),
                    ('Brief y guion', 'Ángulo, gancho y mensaje claros para cada video.'),
                    ('Producción', 'Grabación, edición y entrega lista para subir.'),
                    ('Medir y mejorar', 'Verde se escala, amarillo se ajusta, rojo cambia la idea.')], 'c4 five')),
            ('Trabajo', 'Videos <b>hechos para pauta.</b>', videos_html, 'Desliza para ver más y toca un video para activar el sonido.', 'trabajo'),
        ],
        'faq': [
            ('¿Los creadores son influenciadores?', 'No necesariamente. Buscamos personas que se parezcan a tu cliente y comuniquen bien, no seguidores.'),
            ('¿Puedo usar los videos en pauta y en redes?', 'Sí. Cada video incluye la cesión de derechos para anuncios y redes de tu marca.'),
            ('¿Qué pasa si un video no queda bien?', 'Si no cumple el guion que aprobaste, lo grabamos de nuevo sin costo.'),
            ('¿Ustedes suben los videos a Meta?', 'La pauta es un servicio aparte. Si la manejamos nosotros, los videos entran directo al sistema de pruebas.'),
            ('¿El producto lo envío yo?', 'Sí. Coordinamos el envío del producto a cada creador.'),
        ],
    },
    'email-marketing': {
        'service': 'Email marketing', 'num': '04', 'title': 'Email marketing',
        'meta': 'Automatizaciones y campañas mensuales en Klaviyo para marcas de ecommerce.',
        'h1': 'Tu lista de correos, <b>vendiendo todos los días.</b>',
        'lead': 'Montamos en Klaviyo las automatizaciones que recuperan ventas y enviamos campañas cada mes. Ochenta por ciento contenido de valor, veinte por ciento promoción.',
        'pills': ['Klaviyo + Shopify'],
        'sections': [
            ('Para quién es', 'Para marcas que tienen clientes <b>y no les vuelven a escribir.</b>',
             cards([('No tienes automatizaciones', 'Quien deja el carrito o compra una vez no vuelve a saber de ti.'),
                    ('Envías correos sin plan', 'Solo escribes cuando hay descuento.'),
                    ('Tu lista no crece', 'No hay forma clara de captar correos en tu tienda.')])),
            ('Qué incluye', 'Montaje una vez, <b>campañas cada mes.</b>',
             bullets([('Configuración de Klaviyo', 'Integración con Shopify y migración de tu lista.'),
                      ('Pop-up de captura', 'Para que tu lista crezca con cada visita.'),
                      ('Bienvenida', 'Cuatro correos: beneficio de entrada, historia de la marca, más vendidos y último llamado.'),
                      ('Carrito y pago abandonado', 'Recordatorio, prueba social y último llamado.'),
                      ('Post-compra', 'Productos que complementan lo que compró.'),
                      ('Recuperación de clientes', 'Tres correos para quienes dejaron de comprar.'),
                      ('Campañas mensuales', 'Doce correos al mes con calendario y segmentación.'),
                      ('Redacción y diseño incluidos', 'Escribimos y diseñamos cada correo y cada automatización con la línea gráfica de tu marca. Tú solo apruebas.'),
                      ('Reporte mensual', 'Cuánto vendió el correo y qué ajustamos.')]),
             '', 'incluye'),
            ('Cómo trabajamos', 'Primero lo que vende solo, <b>después las campañas.</b>',
             cards([('Montaje', 'Configuramos Klaviyo, la captura y las automatizaciones.'),
                    ('Calendario', 'Planeamos el mes según tus lanzamientos y fechas clave.'),
                    ('Diseño y envío', 'Cada correo con la línea gráfica de tu marca.'),
                    ('Lectura', 'Revisamos aperturas, clics y ventas para ajustar el siguiente mes.')], 'c4')),
            ('Trabajo', 'Correos que <b>hemos diseñado.</b>', emails_html, 'Desliza para ver más. Puedes hacer scroll dentro de cada correo.', 'trabajo'),
        ],
        'faq': [
            ('¿Necesito tener Klaviyo?', 'Sí. El plan de Klaviyo lo pagas directamente; si no tienes cuenta, la creamos contigo.'),
            ('¿Puedo contratar solo el montaje?', 'Sí. El montaje de automatizaciones es un pago único y las campañas mensuales son opcionales.'),
            ('¿Quién escribe y diseña los correos?', 'Nosotros: redacción y diseño de todas las piezas gráficas, con el tono y la línea gráfica de tu marca. Tú solo apruebas antes de enviar.'),
            ('¿Cuándo están funcionando las automatizaciones?', 'En 15 días hábiles. Si no, te devolvemos el 20% del montaje.'),
        ],
    },
    'growth-partner': {
        'service': 'Growth Partner', 'num': '05', 'title': 'Growth Partner',
        'meta': 'Sitio, pauta, contenido y email operados por un solo equipo, con el pago atado a tus ventas.',
        'h1': 'Un solo equipo para crecer, <b>con nuestro pago atado a tus ventas.</b>',
        'lead': 'Sitio, pauta, contenido y email operados juntos, con una sola estrategia y un solo reporte. Parte de lo que cobramos depende de lo que vendes.',
        'pills': ['Los cuatro servicios', 'Diseño gráfico incluido', '$7.000.000 al mes + 5% de la venta neta'],
        'sections': [
            ('Para quién es', 'Para marcas que ya venden <b>y quieren un socio, no cuatro proveedores.</b>',
             cards([('Coordinas a varios proveedores', 'Cada uno ve su parte y nadie responde por el resultado completo.'),
                    ('Quieres crecer con orden', 'Necesitas que el anuncio, la tienda y el correo empujen en la misma dirección.'),
                    ('Buscas incentivos alineados', 'Prefieres que a tu agencia le vaya bien solo si a ti te va bien.')])),
            ('Qué incluye', 'Los cuatro servicios, <b>operados como uno.</b>',
             bullets([('Optimización del sitio para conversión', 'Mejoras mensuales de la tienda con base en sus datos, con los banners y piezas gráficas que necesite.'),
                      ('Pauta enfocada en conversión', 'Gestión de Meta con revisión diaria, reporte semanal y 15 piezas gráficas al mes.'),
                      ('Contenido UGC', 'Diez videos al mes con estrategia, creadores y análisis.'),
                      ('Email marketing', 'Automatizaciones y campañas mensuales en Klaviyo, con redacción y diseño incluidos.'),
                      ('Sesión estratégica mensual', 'Revisamos números y definimos el foco del mes siguiente.'),
                      ('Dashboard en vivo en Orbit', 'Ventas, pauta y correo actualizados cada 3 minutos.'),
                      ('Reporte mensual en una página', 'Ventas, pauta, tienda y correo en un solo lugar.'),
                      ('Análisis de unit economics', 'Cuánto te queda de verdad por cada venta, producto por producto.')]),
             '', 'incluye'),
            ('Por qué junto', 'Una estrategia, <b>no cuatro.</b>',
             cards([('El mismo mensaje en todas partes', 'El anuncio, la página y el correo cuentan la misma historia.'),
                    ('Decisiones con todos los datos', 'Vemos la pauta, la tienda y el correo al mismo tiempo.'),
                    ('Incentivos alineados', 'El 5% de la venta neta hace que tu crecimiento sea también el nuestro.')])),
        ],
        'faq': [
            ('¿Qué es la venta neta?', 'Las ventas de tu tienda menos descuentos y devoluciones. Sobre esa cifra se calcula el 5%.'),
            ('¿La inversión en anuncios está incluida?', 'No. La inversión la pagas directamente a Meta.'),
            ('¿Qué pasa si no se cumplen los objetivos?', 'Si a los 90 días no cumplimos los objetivos que acordamos al inicio, el siguiente mes no pagas el valor fijo.'),
            ('¿Tengo que diseñar algo?', 'No. Las piezas gráficas de la tienda, los anuncios (15 al mes) y los correos las diseñamos nosotros. Tú solo apruebas.'),
            ('¿Puedo empezar con un solo servicio?', 'Sí. Cada servicio se puede tomar por separado y pasar a Growth Partner cuando tenga sentido.'),
        ],
    },
}

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for slug, s in SERVICES.items():
        (OUT / f'{slug}.html').write_text(page(s))
        print('servicios/%s.html' % slug)
