SELECT customers.name
FROM customers
INNER JOIN legal_person
ON customers.id = legal_person.id_customers;