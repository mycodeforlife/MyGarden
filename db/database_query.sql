create database mygarden;
use database mygarden;
create table gardentools(Name varchar(32),Description varchar(1000),Dimensions varchar(100),Warning varchar(1000));
drop table gardentools;

insert into gardentools(Name,Description,Dimensions,Warning) values ('pruners', 'used for trimming branches, leaf', '7 to 10 inch', 'use lock when not used, keep it away from children');
insert into gardentools(Name,Description,Dimensions,Warning) values ('Gloves', 'Use gloves to make sure hands are protected when working in garden', 'comes in Small, Medium and Large size', 'Clean after usage and keep it in closed box to prevent insects stay inside gloves');
insert into gardentools(Name,Description,Dimensions,Warning) values ('Shovel', 'Used for mixing and shoveling soil', 'Handle comes in 3 fee to 5 feet (you can change based on your needs)','Clean and keep it dry to make sure shovel is in good state');
