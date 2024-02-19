create database imbd;

use imbd;

create table movies(
id int auto_increment primary key,
name varchar(200) not null ,
language varchar(200) not  null,
year varchar(200) not null
);


insert into movies(name,language,year) values('rdx','malayalam','2023');
insert into movies(name,language,year) values('kgf','telengu','2022');
insert into movies(name,language,year) values('kavalan','tamil','2023');
insert into movies(name,language,year) values('kotha','malayalam','2023');

select * from movies;


create table review(
id int auto_increment primary key,
user varchar(200) not null,
comment varchar(200) not null,
rating int check(rating<6),
movie_id int not null,
foreign key(movie_id) references movies(id) on delete cascade
);

insert into review(user,comment,rating,movie_id) values('anu','good',4,2);
insert into review(user,comment,rating,movie_id) values('sreethu',' very good',5,3);
insert into review(user,comment,rating,movie_id) values('hari','not bad',2,4);

select* from review;

select m.name,r.user,r.comment,r.rating  from movies as m,review as r where m.id=r.movie_id and m.name='kgf';

select m.name,r.rating from movies as m,review as r where m.id=r.movie_id;

select m.name,r.rating,r.user,r.comment from movies as m inner join review as r on m.id=r.movie_id;

select m.name,r.rating,r.user,r.comment from movies as m left join review as r on m.id=r.movie_id;