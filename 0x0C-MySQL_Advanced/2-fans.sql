-- Rank countries by the number of metal fans
SELECT origin, SUM(fans) country_fans
FROM metal_bands
GROUP BY origin
ORDER BY country_fans DESC;
