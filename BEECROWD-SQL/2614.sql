SELECT name, rentals_date 
FROM customers
INNER JOIN rentals ON customers.id = rentals.id_customers
WHERE DATE_PART('month', rentals_date) = 9
AND DATE_PART('year', rentals_date) = 2016;