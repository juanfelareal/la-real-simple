"""Arma la vista previa de Bloki en un solo HTML (CSS, JS e imágenes embebidos).

Uso: python3 bloki-preview/build.py <salida.html>
El resultado no carga nada de blokipresente.co, así que sirve como vista previa privada.
"""
import base64
import json
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"


def data_uri(name):
    path = ASSETS / name
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


html = (ROOT / "index.html").read_text()
head, body = html.split("<body>", 1)
body = body.split("</body>", 1)[0]

css = "\n".join((ASSETS / f).read_text() for f in ("bloki-landing.css", "bloki-shopify.css"))
js = (ASSETS / "bloki-landing.js").read_text()

# Sin IDs de variante el botón de compra muestra el aviso de vista previa en vez de ir al carrito.
cfg_re = re.compile(r'(<script type="application/json" id="bk-config">)(.*?)(</script>)', re.S)
cfg = json.loads(cfg_re.search(body).group(2))
cfg["variants"] = {}
body = cfg_re.sub(lambda m: m.group(1) + json.dumps(cfg, ensure_ascii=False) + m.group(3), body)
body = body.replace('<script defer src="assets/bloki-landing.js"></script>',
                    "<script>\n" + js + "\n</script>")

out = f"""<title>Bloki vista previa</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Mono:wght@400&display=swap">
<style>
{css}
:root{{color-scheme:light}}
</style>
{body.strip()}
"""
out = re.sub(r'assets/([\w.-]+\.(?:jpg|png|svg|webp))', lambda m: data_uri(m.group(1)), out)

Path(sys.argv[1]).write_text(out)
print(f"{sys.argv[1]}: {len(out) // 1024} KB")
