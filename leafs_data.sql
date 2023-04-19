drop database if exists leafs;
create database leafs;

use leafs;

create table players (
player_id INT primary key auto_increment,
first_name varchar(25),
last_name varchar(50),
position varchar(5),
number varchar(3) not null,
country varchar(50)
);

create table stats (
player_id int primary key auto_increment,
constraint `players_fk_stats` foreign key (`player_id`) references `leafs`.`players` (`player_id`),
player_name varchar (50),
goals varchar(5),
assists varchar(5),
points varchar(5)
);

insert into leafs.players values(1, 'Auston', 'Matthews', 'C', 34, 'USA');
insert into leafs.players values(2, 'Mitch', 'Marner', 'RW', 16, 'CAN');
insert into leafs.stats values(1, 'Matthews', 0, 0, 0);
insert into leafs.stats values(2, 'Marner', 0, 0, 0);
