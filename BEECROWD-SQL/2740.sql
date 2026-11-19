SELECT name
FROM (
  (SELECT CONCAT('Podium: ', team) AS name, 1 AS grp, position
   FROM league
   ORDER BY position ASC
   LIMIT 3)

  UNION ALL

  (SELECT CONCAT('Demoted: ', team), 2, position
   FROM league
   ORDER BY position DESC
   LIMIT 2)
) t
ORDER BY grp, position;