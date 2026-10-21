# Nicolás Alderete - Data & Operations

Portfolio público: https://nicoalderete.github.io/

## Contenido

- Experiencia aplicada: bajas y retención, agenda de revisiones y reporting operativo.
- Proyecto Python + SQL: Top 100 Airports.
- Proyectos académicos de Business Intelligence: Power BI y Tableau.
- Sitio completo y CV en español e inglés.

Los casos profesionales describen contribuciones dentro de un trabajo de equipo. Las demostraciones usan registros ficticios creados para el portfolio, sin bases internas ni código de producción. Ver [metodología y límites](docs/METHODOLOGY.md).

## Desarrollo

Sitio estático sin dependencias JavaScript ni proceso de compilación para publicar. GitHub Pages sirve los archivos del repositorio; `.nojekyll` evita procesamiento Jekyll.

El contenido ES/EN se mantiene en `scripts/build_portfolio.py`:

```sh
python3 scripts/build_portfolio.py
python3 -m http.server 8765
```

CSS compartido: `assets/css/portfolio.css`. Interacciones: `assets/js/portfolio.js` (filtros, ampliación de capturas y demos).

Para regenerar los CV se necesita Python con ReportLab y las fuentes DejaVu Sans:

```sh
python3 scripts/build_cv.py
```

Los enlaces originales a `casos/powerbi.html` y `casos/tableau.html` se conservan. La navegación de idioma mantiene el caso actual. No hay formularios de contacto ni recopilación de datos personales.
