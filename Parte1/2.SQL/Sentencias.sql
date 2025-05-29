-- ¿Quiénes son los clientes que realizaron pedidos en el último mes?

SELECT DISTINCT c.idClient, c.name, c.lastname, c.email, c.spendedAmount FROM client AS c JOIN orders AS ord ON ord.idClient = c.idClient WHERE ord.orderDate BETWEEN
    DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m-01')
  	AND LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))


-- ¿Cuáles son los productos más vendidos?
SELECT idProduct, productName FROM products ORDER BY timesBought DESC LIMIT 10;

-- ¿Cuál es el total facturado por cada cliente?
SELECT idClient, spendedAmount FROM client;