SELECT *
FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA' AND CustomerID<10 OR CustomerID>80 OR PostalCode IS NULL
ORDER BY Country DESC, CustomerName DESC
LIMIT 10;

UPDATE Customers
SET CustomerName='XXXXX udsojss'
WHERE CustomerID=89;