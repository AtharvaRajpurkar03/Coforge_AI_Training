create database Coforge_db;
use coforge_db;

create table Employee(
EmpId int primary key auto_increment,
EmpName varchar(20),
EmpAge int,
EmpEmail varchar(50),
EmpSalary decimal(10,2),
EmpCity varchar(20) 
);


INSERT INTO Employee (EmpName, EmpAge, EmpEmail, EmpSalary, EmpCity) VALUES
('Shiv',23,'shiv1@gmail.com',45000,'Pune'),
('Atharva',22,'atharva1@gmail.com',42000,'Mumbai'),
('Pranjali',24,'pranjali1@gmail.com',48000,'Nagpur'),
('Akash',25,'akash1@gmail.com',50000,'Delhi'),
('Hitesh',23,'hitesh1@gmail.com',46000,'Pune'),
('Sahil',22,'sahil1@gmail.com',41000,'Mumbai'),
('Shreyansh',24,'shreyansh1@gmail.com',47000,'Hyderabad'),
('Prince',26,'prince1@gmail.com',55000,'Indore'),
('Rohit',27,'rohit1@gmail.com',52000,'Pune'),
('Aman',25,'aman1@gmail.com',49000,'Delhi'),
 
('Neha',24,'neha1@gmail.com',45000,'Mumbai'),
('Pooja',23,'pooja1@gmail.com',43000,'Pune'),
('Kunal',28,'kunal1@gmail.com',60000,'Bengaluru'),
('Vikas',29,'vikas1@gmail.com',62000,'Chennai'),
('Anjali',22,'anjali1@gmail.com',40000,'Nagpur'),
('Sneha',24,'sneha1@gmail.com',47000,'Pune'),
('Nikhil',26,'nikhil1@gmail.com',53000,'Hyderabad'),
('Harsh',27,'harsh1@gmail.com',58000,'Mumbai'),
('Tushar',25,'tushar1@gmail.com',51000,'Delhi'),
('Deepak',30,'deepak1@gmail.com',70000,'Bengaluru'),
 
('Shivam',24,'shivam1@gmail.com',45000,'Pune'),
('Atharva2',23,'atharva2@gmail.com',42000,'Mumbai'),
('Pranjal',25,'pranjal1@gmail.com',48000,'Nagpur'),
('Akshay',26,'akshay1@gmail.com',50000,'Delhi'),
('Hitesh2',24,'hitesh2@gmail.com',46000,'Pune'),
('Sahil2',23,'sahil2@gmail.com',41000,'Mumbai'),
('Shrey',25,'shrey1@gmail.com',47000,'Hyderabad'),
('Prince2',27,'prince2@gmail.com',55000,'Indore'),
('Rohit2',28,'rohit2@gmail.com',52000,'Pune'),
('Aman2',26,'aman2@gmail.com',49000,'Delhi'),
 
('Neha2',25,'neha2@gmail.com',45000,'Mumbai'),
('Pooja2',24,'pooja2@gmail.com',43000,'Pune'),
('Kunal2',29,'kunal2@gmail.com',60000,'Bengaluru'),
('Vikas2',30,'vikas2@gmail.com',62000,'Chennai'),
('Anjali2',23,'anjali2@gmail.com',40000,'Nagpur'),
('Sneha2',25,'sneha2@gmail.com',47000,'Pune'),
('Nikhil2',27,'nikhil2@gmail.com',53000,'Hyderabad'),
('Harsh2',28,'harsh2@gmail.com',58000,'Mumbai'),
('Tushar2',26,'tushar2@gmail.com',51000,'Delhi'),
('Deepak2',31,'deepak2@gmail.com',70000,'Bengaluru');


select * from Employee;
select EmpName from Employee;
select EmpName, EmpSalary from Employee;
select EmpName, EmpAge, EmpCity from Employee;
select distinct EmpCity from Employee;
select EmpName, EmpCity from Employee where EmpCity="Pune";
select EmpName, EmpSalary from Employee where EmpSalary>50000;
select * from Employee where EmpAge<25;
select * from Employee where EmpSalary=45000;
select * from Employee where EmpCity <> "Mumbai";
select * from Employee where EmpSalary between 40000 and 50000;
select * from Employee where EmpCity in ("Mumbai","Pune");
select * from Employee where EmpAge between 23 and 27;
select * from Employee where EmpCity="Pune" and EmpSalary>45000;
select * from Employee where EmpName like '%sh%';
select * from Employee order by EmpSalary desc;
select * from Employee order by EmpSalary desc limit 5;
select * from Employee order by EmpCity, EmpSalary desc;
select count(*) as 'Total_Employee' from Employee;
select max(EmpSalary) as 'Max Salary' from Employee;
select min(EmpSalary) as 'Min Salary' from Employee;
select round(avg(EmpSalary),2) as 'Avg Salary' from Employee;
select sum(EmpSalary) as 'Total Salary' from Employee;
select count(*) as 'Salary Count' from Employee where EmpSalary>50000;
select max(EmpSalary) - min(EmpSalary) from Employee;
select EmpCity,count(*) as Employee_Count from Employee group by EmpCity;
select EmpCity,count(*) as Employee_Count from Employee group by EmpCity,EmpName;
select EmpCity,max(EmpSalary),min(EmpSalary),avg(EmpSalary),sum(EmpSalary) from Employee group by EmpCity;
select EmpCity,count(*) as Emp_Count from Employee group by EmpCity having Emp_Count>4;
select EmpCity, round(avg(EmpSalary),2) as AvgSalary from Employee group by EmpCity having AvgSalary>50000;
select EmpAge,count(*) as EmpCount from Employee group by EmpAge;
