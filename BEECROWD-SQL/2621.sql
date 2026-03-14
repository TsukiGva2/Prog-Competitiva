SELECT products.name
FROM products
INNER JOIN providers
ON products.id_providers = providers.id
WHERE providers.name LIKE 'P%'
AND products.amount BETWEEN 10 AND 20;