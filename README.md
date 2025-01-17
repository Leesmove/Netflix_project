# Netflix Project

Este proyecto analiza los datos de Netflix para identificar tendencias, patrones y oportunidades de mejora. El análisis sigue las fases del proyecto: 
**Formular preguntas, Adquirir datos, Preparar datos, Analizar, Compartir y Actuar**.

## Estructura del Proyecto

- **`data/`**: Contiene los datos originales y procesados.
- **`scripts/`**: Incluye los scripts Python y SQL para procesar y analizar los datos.
- **`docs/`**: Documentación específica de cada fase del proyecto.
- **`README.md`**: Descripción general del proyecto.

## Fases del Proyecto

1. **Formular preguntas**
   - ¿Qué géneros tienen las mejores calificaciones promedio en IMDb?
   - ¿Qué países producen más contenido para Netflix?
   - ¿Cuáles son las películas/series más populares por año?

2. **Adquirir y preparar datos**
   - Los datos se obtuvieron de [fuente de datos].
   - Limpieza realizada en Python, resultados almacenados en `Netflix_cleaned.csv`.

3. **Procesar datos**
   - Carga a MySQL usando `Carga_mysql.py`.
   - Consultas SQL documentadas en `scripts/consultas.sql`.

4. **Análisis**
   - Principales hallazgos documentados en `docs/README_phase4.md`.

5. **Compartir**
   - Resultados clave y visualizaciones disponibles en `docs/`.

6. **Actuar**
   - Recomendaciones finales basadas en los análisis.

## Instrucciones de Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Leesmove/Netflix_project.git
   cd Netflix_project