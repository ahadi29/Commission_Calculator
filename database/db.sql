create database commission;

use commission;

-- creating a table to store user id and password 
create table ADMIN(
	usrId varchar(25) PRIMARY KEY,
	pass varchar(25)
);

-- create TABLE emp which contains emp details
create table EMP(
	empid Integer PRIMARY KEY,
	ename varchar(255),
	loc varchar(255),
	sal INTEGER 
);

-- creating a table to calaculate commision
CREATE TABLE CALC(
  empId INTEGER,
  sales INTEGER,
  commision double as (sales*0.10),
  FOREIGN KEY (empId) REFERENCES EMP(empId)
);

insert into ADMIN value('xyz','123456'); 
insert into EMP values(111,'abc','chennai',10000);
insert into CALC(empId,sales) values(111,10000);
select * from ADMIN;
select * from EMP;
Select * from CALC;

drop table CALC;

