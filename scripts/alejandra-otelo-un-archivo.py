#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma una copia de la landing con todo adentro, para revisar sin servidor.

La version publicada carga las fotos y las tipografias desde
assets/alejandra-otelo/. Eso hace que la pagina aparezca de inmediato, pero
tambien que no se pueda abrir con doble clic: Chrome bloquea las mascaras CSS
cuando el archivo viene de file://, y el logotipo desaparece.

    python3 scripts/alejandra-otelo-un-archivo.py [salida.html]
"""
import base64, io, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTE = os.path.join(RAIZ, 'assets', 'alejandra-otelo.html')
SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, 'alejandra-otelo-un-archivo.html')

TIPOS = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png',
         '.webp': 'image/webp', '.woff2': 'font/woff2', '.svg': 'image/svg+xml'}

s = io.open(FUENTE, encoding='utf-8').read()


def incrustar(m):
    ruta = os.path.normpath(os.path.join(RAIZ, 'assets', m.group(1)))
    ext = os.path.splitext(ruta)[1].lower()
    with open(ruta, 'rb') as f:
        return 'data:%s;base64,%s' % (TIPOS[ext], base64.b64encode(f.read()).decode())


s, n = re.subn(r'\.\./assets/(alejandra-otelo/[^"\')]+)', incrustar, s)
io.open(SALIDA, 'w', encoding='utf-8').write(s)
print('%d archivos incrustados -> %s (%.1f MB)' % (n, SALIDA, os.path.getsize(SALIDA) / 1048576.0))
