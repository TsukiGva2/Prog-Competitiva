SELECT products.name, providers.name
FROM providers
INNER JOIN products
ON providers.id = products.id_providers
WHERE providers.name = 'Ajax SA';