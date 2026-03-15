SELECT products.name, categories.name
FROM products
INNER JOIN categories
ON products.id_categories = categories.id
WHERE products.amount > 100
AND products.id_categories IN (1,2,3,6,9)
ORDER BY products.id_categories ASC;