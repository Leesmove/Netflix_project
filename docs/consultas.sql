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

-- Fase 3: Procesar los datos
-- Convertir nombres de géneros a minúsculas (si necesario):
UPDATE netflix 
SET genres = LOWER(genres);

-- Crear vistas para facilitar análisis posteriores:
CREATE VIEW netflix_top_rated AS 
SELECT title, genres, imdbAverageRating 
FROM netflix 
WHERE imdbAverageRating >= 8.0;

-- Fase 4: Análisis
-- Promedio de calificaciones por género
SELECT genres, AVG(imdbAverageRating) AS avg_rating 
FROM netflix 
GROUP BY genres 
ORDER BY avg_rating DESC;

-- Títulos con más votos
SELECT title, imdbNumVotes 
FROM netflix 
ORDER BY imdbNumVotes DESC 
LIMIT 10;

-- Fase 5: Compartir
-- Para compartir resultados, crear tablas resumen o exportar los resultados a formatos como CSV:
-- Exportar datos a un archivo:
SELECT * 
INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/export.csv"
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
FROM netflix;

-- Fase 6: Actuar
-- Géneros que Netflix debería expandir basándose en calificaciones altas y pocos títulos:
SELECT genres, COUNT(*) AS num_titles, AVG(imdbAverageRating) AS avg_rating 
FROM netflix 
GROUP BY genres 
HAVING avg_rating > 8.0 AND num_titles < 20;



