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

## Visualizaciones en Power BI

Las siguientes visualizaciones fueron creadas en Power BI para analizar los datos de Netflix:

- **Mapa de burbujas:** Muestra la distribución de contenido por país.
- **Tendencias anuales:** Evolución del número de títulos a lo largo de los años.
- **Géneros populares:** Comparación de los géneros más vistos.

[Dashboard Principal](https://drive.google.com/file/d/188co2WeCRRWTw_6nYqp4rukuDy_kxEhs/view?usp=sharing)

## Acceso al Dashboard  

Puedes ver el informe interactivo de Power BI en el siguiente enlace:  

[Ver Dashboard en Power BI](https://app.powerbi.com/reportEmbed?reportId=72e691af-4da4-457b-b5f9-6d0d4bb4e0c5&autoAuth=true&ctid=dd505be5-ec69-47f5-92df-caa55febf5fa))


## Instrucciones de Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Leesmove/Netflix_project.git
   cd Netflix_project
