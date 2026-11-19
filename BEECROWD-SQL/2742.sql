SELECT l.name, ROUND(l.omega*1.618, 3) AS "Fator N"
FROM life_registry AS l
INNER JOIN dimensions AS d
ON l.dimensions_id = d.id
WHERE (d.name = 'C875'
OR d.name = 'C774')
AND l.name ILIKE 'Richard%'
ORDER BY l.omega;