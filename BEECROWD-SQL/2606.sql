SELECT p.id, p.name FROM products AS p
INNER JOIN categories AS c 
ON p.id_categories = c.id
WHERE c.name LIKE 'super%';