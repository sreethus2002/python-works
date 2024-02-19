create database cakehuts;
use cakehuts;
create table cakes(
       id int not null auto_increment primary key,
       name varchar(200) not null unique
);
insert into cakes(name) values ('blue berry');
insert into cakes(name) values ('vancho');
insert into cakes(name) values ('chocalate');
insert into cakes(name) values ('butter scotch');
select * from cakes;
create table cake_variants(
	   id int not null auto_increment primary key,
       weight enum('500gm','1kg','2kg') default '1kg',
       shape varchar (200) not null,
       price int not null,
       cake_id int not null,
       foreign key(cake_id) references cakes(id) on delete cascade
);
insert into cake_variants(weight,price,shape,cake_id) values ('1kg',700,'circle',1);
insert into cake_variants(weight,price,shape,cake_id) values ('2kg',800,'circle',1);
insert into cake_variants(weight,price,shape,cake_id) values ('1kg',500,'circle',2);
insert into cake_variants(weight,price,shape,cake_id) values ('2kg',750,'circle',3);
insert into cake_variants(weight,price,shape,cake_id) values ('1kg',1000,'circle',3);
select * from cake_variants;

select c.name,cv.price from cakes as c left join cake_variants as cv on c.id=cv.cake_id order by cv.price desc limit 1;