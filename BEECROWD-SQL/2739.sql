SELECT name, CAST(DATE_PART('day', payday) AS INT) AS day
FROM loan;