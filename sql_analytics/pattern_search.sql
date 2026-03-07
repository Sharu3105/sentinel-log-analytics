-- Find IPs that would be flagged as 'High Risk' (Relational Division logic)
-- Any IP that has accessed more than 3 distinct sensitive 'admin' endpoints
SELECT ip_address
FROM LogTable
WHERE endpoint LIKE '/admin/%'
GROUP BY ip_address
HAVING COUNT(DISTINCT endpoint) >= 3;
