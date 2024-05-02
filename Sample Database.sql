create database if not exists Abels_Store;

use Abels_Store;


create table products(
product_id INT PRIMARY KEY AUTO_INCREMENT,
product_name VARCHAR(255),
price_in_USD FLOAT,
discount_eligible ENUM ('Yes', 'No')
);


create table suppliers(
supplier_id INT PRIMARY KEY,
supplier_name VARCHAR(255),
supplier_email VARCHAR(255),
product_id INT,
FOREIGN KEY (product_id) REFERENCES products(product_id)
);



create table stores(
store_id INT PRIMARY KEY,
city VARCHAR(255),
total_sales_revenue FLOAT,
store_rating_1_to_5 INT
);


INSERT INTO products(product_name,price_in_USD,discount_eligible)
VALUES ('T-shirts', 10.00, 'Yes'), ('Pants', 11.00, 'Yes'), ('Shoes', 15.00, 'Yes');


INSERT INTO products(product_name,price_in_USD,discount_eligible)
VALUES ('Belts', 7.50, 'Yes'), ('Laptops', 300, 'No'), ('Air Conditioners', 400, 'No'), ('Playstation 5', 500, 'No');

INSERT INTO products(product_name,price_in_USD,discount_eligible)
VALUES ('Bread', 3, 'No'), ('Canned Beans', 3, 'No'), ('Orange Juice', 5, 'No'), ('Cereal', 7, 'No'), ('Sliced Cheese', 4, 'No'), ('Sliced Turkey', 5, 'No');

INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, product_id)
VALUES (9100, 'Farmers Union Inc.', 'farmers_union@gmail.com', 8), (8261, 'General Electronics', 'ge@gmail.com', 7);



INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, product_id)
VALUES (2500, 'General Mills', 'generalmills@gmail.com', 11), (4877, 'Senor Joses', 'senorjoses@yahoo.com', 9), (1012, 'Kitchen Dreams', 'kitchendreams@gmail.com', 12);


INSERT INTO stores(store_id, city, total_sales_revenue, store_rating_1_to_5)
VALUES (123, 'WASHINGTON DC', 3400030, 4), (411, 'NEW YORK CITY', 4322032, 4), (132, 'BOSTON', 2441000, 3), (762, 'ATLANTA', 8900472, 2), (982, 'Los Angeles', 782377, 5);






select * from products;

select * from suppliers;

select * from stores;
