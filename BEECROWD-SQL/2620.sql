SELECT customers.name, orders.id
FROM customers
INNER JOIN orders
ON customers.id = orders.id_customers
WHERE EXTRACT('month' FROM orders.orders_date) <= 6;