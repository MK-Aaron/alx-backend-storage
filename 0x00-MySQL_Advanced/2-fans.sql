-- ranks country origin of bands

SELECT origin, SUM(fans) AS nb fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
