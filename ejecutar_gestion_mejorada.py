"""Ejecutor visual de la app de alquileres, sin modificar su lógica de negocio.

Ejecutá ``streamlit run ejecutar_gestion_mejorada.py`` desde esta carpeta.
"""

import importlib
from pathlib import Path

import estilos_gestion_alquileres as estilos


pagina_original = Path(__file__).with_name("pagina.py")
if not pagina_original.is_file():
    raise FileNotFoundError(
        "No se encontró pagina.py junto a ejecutar_gestion_mejorada.py."
    )

importlib.reload(estilos)
estilos.aplicar_estilo_gestion()
codigo = estilos.preparar_cromo_profesional(
    pagina_original.read_text(encoding="utf-8")
)
exec(compile(codigo, str(pagina_original), "exec"), globals(), globals())
