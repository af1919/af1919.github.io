USE Abels_Store;
select * from stores;

insert into stores(store_id, city, total_Sales_revenue, store_rating_1_to_5)
values(432,'Baltimore',3219200,2),(662,'Miami',4339921,4), (772,'Dallas', 3443128, 3), (828, 'Chicago', 3555200, 2);

select * from stores;

update stores
set city = 'Boston'
where store_id = 132;

select * from stores;

update stores
set city = 'New York City'
where store_id = 411;

update stores
set city = 'Atlanta'
where store_id = 762;

insert into stores
values (555, 'Salt Lake City', 4332128, 3), (100, 'Arlington', 4388000, 4), (113, 'Houston', 2312000, 1), (989, 'Las Vegas', 28712300,4), (899, 'Richmond', 43873200, 4);


select * from stores;


insert into stores
values (777, 'Flint',1092330, 3), (111, 'San Francisco',7229820, 3), (527, 'Charolette', 322124, 1), (211, 'Austin', 8721000, 5);


select * from stores;

select * from suppliers;

insert into suppliers
values(8892, 'Tokoyo Tech', 'tytech@yahoo.com', 1), (1920, 'Samson Appliances Inc.', 'SAppliances@yahoo.com', 10), (4321, 'Good Meals LLC','goodmeals@gmail.com' ,4), (9811, 'Nestle USA Inc.', 'nestleusa@yahoo.com', 3);

select * from suppliers;

select * from products;

update suppliers
set product_id = 5
where supplier_id = 8892;

select * from suppliers;

insert into suppliers
values (3872, 'Too Good To Go Foods Inc.', 'TGTG@aol.com', 8), (1000, 'Pepsi Cola USA','pepsiusa@yahoo.com',3), (4598, 'Bellos Kitchen Inc', 'belloskitchen@gmail.com',11), (3772, 'Fanta Films LLC', 'fantafilmstudios@gmail.com',5);


select * from products;


insert into products
values (15, 'Brazen Beef', 10, 'No'), (16, 'Milk', 6, 'Yes'),(17, 'Paper Plates', 7, 'No'), (18, 'Salmon', 9, 'No'), (19, 'Shrimp', 11, 'No')

-- This 





