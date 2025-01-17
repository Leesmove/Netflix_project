-- Fase 2: Adquirir y preparar datos
-- Verificar la distribución de años
SELECT releaseYear, COUNT(*) 
FROM netflix 
GROUP BY releaseYear 
ORDER BY releaseYear;

-- Identificar valores nulos en columnas clave
SELECT * 
FROM netflix 
WHERE imdbId IS NULL OR imdbAverageRating IS NULL;

-- Fase 4: Análisis
-- Promedio de calificaciones por género
SELECT genres, AVG(imdbAverageRating) AS avg_rating 
FROM netflix 
GROUP BY genres 
ORDER BY avg_rating DESC;
