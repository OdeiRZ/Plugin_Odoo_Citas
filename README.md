# Plugin Odoo Citas

Módulo (addon) para Odoo 8.0 que añade un modelo de "citas célebres" (frases con autor) gestionable desde el propio ERP.

## Características

- Nuevo modelo `citas.cita` con los campos: autor, texto de la cita, fecha de visualización y orden de visualización.
- Vistas de lista (tree), formulario y búsqueda integradas en el menú de Odoo, bajo la entrada "Citas".
- Alta, listado, consulta, modificación y baja de citas desde la interfaz estándar de Odoo (sin necesidad de código adicional).
- Permisos de acceso al modelo definidos en `security/ir.model.access.csv`.
- Datos de demostración incluidos (`citas_data.xml`) para probar el módulo tras instalarlo.

## Tecnologías

- Python (API de modelos de Odoo: `models.Model`, `fields`)
- XML (vistas y datos de Odoo)
- Odoo / OpenERP 8.0

## Instalación / Cómo ejecutarlo

1. Copia la carpeta `citas/` (con todo su contenido) dentro del directorio `addons` de tu servidor Odoo.
2. Si el servidor Odoo ya está en marcha, reinícialo para que detecte el nuevo módulo.
3. Desde Odoo, ve a **Configuración → Módulos → Módulos locales**, busca "Citas" e instálalo.
4. Accede al nuevo menú "Citas" para crear, listar y gestionar tus citas célebres.

Desarrollado y probado sobre Odoo 8.0; no se garantiza su funcionamiento en versiones anteriores.

## Licencia

GPL versión 3 (ver archivo [LICENSE](LICENSE)).
