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
insert into leafs.players values(3, 'Morgan', 'Reilly', 'LD', 44, 'CAN');
insert into leafs.stats values(3, 'Reilly', 0, 0, 0);
insert into leafs.players values(4, 'Ryan', "O'Reilly", 'C', 90, 'CAN');
insert into leafs.stats values(4, "O'Rielly", 0, 0, 0);
insert into leafs.players values(5, 'Michael', "Bunting", 'LW', 58, 'CAN');
insert into leafs.stats values(5, "Bunting", 0, 0, 0);
insert into leafs.players values(6, 'Calle', "Janrkrok", 'LW', 19, 'SWE');
insert into leafs.stats values(6, "Jarnkrok", 0, 0, 0);
insert into leafs.players values(7, 'William', "Nylander", 'RW', 88, 'SWE');
insert into leafs.stats values(7, "Nylander", 0, 0, 0);
insert into leafs.players values(8, 'John', "Tavares", 'C', 91, 'CAN');
insert into leafs.stats values(8, "Tavares", 0, 0, 0);
insert into leafs.players values(9, 'David', "Kampf", 'C', 64, 'SWE');
insert into leafs.stats values(9, "Kampf", 0, 0, 0);
insert into leafs.players values(10, 'Alex', "Kerfoot", 'LW', 15, 'CAN');
insert into leafs.stats values(10, "Kerfoot", 0, 0, 0);
insert into leafs.players values(11, 'TJ', "Brodie", 'LD', 78, 'CAN');
insert into leafs.stats values(11, "Brodie", 0, 0, 0);
insert into leafs.players values(12, 'Mark', "Giordano", 'LD', 55, 'CAN');
insert into leafs.stats values(12, "Giordano", 0, 0, 0);
insert into leafs.players values(13, 'Luke', "Schenn", 'LD', 2, 'CAN');
insert into leafs.stats values(13, "Schenn", 0, 0, 0);
insert into leafs.players values(14, 'Justin', "Holl", 'RD', 3, 'CAN');
insert into leafs.stats values(14, "Holl", 0, 0, 0);
insert into leafs.players values(15, 'Jake', "McCabe", 'LD', 22, 'CAN');
insert into leafs.stats values(15, "McCabe", 0, 0, 0);
insert into leafs.players values(16, 'Timothy', "Liljegren", 'RD', 37, 'SWE');
insert into leafs.stats values(16, "Liljegren", 0, 0, 0);
insert into leafs.players values(17, 'Zach', "Aston-Reese", 'LW', 12, 'CAN');
insert into leafs.stats values(17, "Aston-Reese", 0, 0, 0);
insert into leafs.players values(18, 'Wayne', "Simmonds", 'RW', 24, 'CAN');
insert into leafs.stats values(18, "Simmonds", 0, 0, 0);

