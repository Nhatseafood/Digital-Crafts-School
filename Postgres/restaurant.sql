CREATE DATABASE restaurant;
\c restaurant;

CREATE TABLE restaurant (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR,
  distance INTEGER NOT NULL,
  stars INTEGER NOT NULL,
  category VARCHAR,
  favorite_dish VARCHAR,
  does_takeout BOOLEAN,
  last_meal DATE
);

insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values('Moon Tower', 2, 4, 'bar', 'Hot Dogs', TRUE, '2018-04-17');



insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values ('Jack in the box', 3, 3, 'Fast Food', 'Tacos', TRUE, '2018-04-22');


insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values ('Pho Spot', 10, 4, 'Vietnamese', 'Pho', TRUE, '2018-04-26');

insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values ('Subway', 20, 5, 'Vietnamese', 'Sandwiches', TRUE, '2018-04-12');

insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values ('Popeyes', 7, 5, 'Fast Food', 'Chicken', TRUE, '2018-03-12');

insert into restaurant(name, distance,stars,category,favorite_dish, does_takeout,last_meal) values ('Quiznos', 7, 4, 'Fast Food', 'Sandwiches', TRUE, '2018-03-13');



SELECT * FROM restaurant WHERE stars = 4;

SELECT favorite_dish FROM restaurant WHERE stars = 4;

SELECT id from restaurant where name = 'Moon Tower';

SELECT * from restaurant where category = 'bar';

select * from restaurant where does_takeout = TRUE;

select * from restaurant where does_takeout = TRUE and category = 'bar';

select * from restaurant where distance = 2;

select * from restaurant where current_date - last_meal > 7 and stars = 4;

select * from restaurant order by distance;

select * from restaurant order by distance limit 2;

select * from restaurant order by stars desc limit 2;

select * from restaurant where distance <=2 order by stars desc limit 2;

select count(*) from restaurant;


select category, avg(stars) from restaurant group by category;

select category, max(stars) from restaurant group by category;

