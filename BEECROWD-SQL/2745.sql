SELECT name, ROUND(salary/10,2) AS tax
FROM people
WHERE salary > 3000;