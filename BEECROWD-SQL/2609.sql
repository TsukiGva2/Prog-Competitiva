SELECT p.name, SUM(p.amount) FROM PRODUCTS AS p
INNER JOIN categories AS c
ON p.id_categories = c.id
GROUP BY c.name;