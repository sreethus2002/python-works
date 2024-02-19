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