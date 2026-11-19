SELECT DISTINCT node_id, 
    CASE
    WHEN pointer IS NULL THEN 'LEAF'
    WHEN node_id NOT IN (SELECT pointer FROM nodes WHERE pointer IS NOT NULL) THEN 'ROOT'
    ELSE 'INNER'
    END AS "type"
FROM nodes
ORDER BY node_id;