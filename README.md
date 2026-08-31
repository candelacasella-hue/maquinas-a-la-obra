# Máquinas a la Obra

Sistema de gestión para un negocio de alquiler de máquinas, renovado con una interfaz sobria, clara y responsive. Mantiene los flujos de clientes, catálogo, alquileres, devoluciones e ingresos.

## Ejecutar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run ejecutar_gestion_mejorada.py
```

En macOS o Linux, activá el entorno con `source .venv/bin/activate`.

## Acceso al módulo de ingresos

Por seguridad, la contraseña no se guarda en el repositorio. Definí la variable de entorno `FINANZAS_PASSWORD` antes de iniciar la app.

PowerShell:

```powershell
$env:FINANZAS_PASSWORD = "elegí-una-clave-segura"
streamlit run ejecutar_gestion_mejorada.py
```

## Publicación en Streamlit Community Cloud

1. Creá una nueva app desde el repositorio.
2. Seleccioná como archivo principal `ejecutar_gestion_mejorada.py`.
3. En **Advanced settings → Secrets**, agregá `FINANZAS_PASSWORD = "tu-clave"`.

La base de datos SQLite es local a cada instancia. Para información persistente en producción, conviene migrarla a una base de datos administrada.
