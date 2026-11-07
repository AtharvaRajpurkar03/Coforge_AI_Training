-- Q001. List all databases on the server. 
show databases;

-- Q002. Select the hsbc_bank database. 
use hsbc_bank;

-- Q003. List all tables in hsbc_bank. 
show tables;

-- Q004. Describe the structure of Employees. 
desc employees;

-- Q005. Describe the structure of Payroll. 
desc payroll;

-- Q006. Display every column of Employees.
select * from employees;

-- Q007. Display employee_id, first_name and last_name only. 
select employee_id, first_name, last_name from employees;

-- Q008. Display distinct designations. 
select distinct designation from employees;

-- Q009. Display distinct department locations. 
SELECT distinct location from departments;

-- Q010. Retrieve all department names and annual budgets. 
select department_name, annual_budget from departments;

-- Q011. Retrieve the first 10 employees ordered by employee_id. 
select * from employees order by employee_id limit 10;

-- Q012. Create a full_name alias by concatenating first_name and last_name. 
select concat(first_name," ",last_name) as full_name from employees;

-- Q013. Show employee name and annualized base salary (base_salary * 12). 
select first_name, last_name, base_salary*12 as annualized_base_salary from employees;

-- Q014. Display all project names, statuses and budgets. 
select project_name, project_status, budget from projects;

-- Q015. List payroll records with calculated net_pay. 
select payroll_id, employee_id, pay_month, net_pay from payroll;

-- Q016. Find employees with base_salary greater than 90000. 
select * from employees where base_salary>90000;

-- Q017. Find employees earning between 60000 and 110000. 
select * from employees where base_salary between 60000 and 110000;

-- Q018. Find employees hired on or after 2024-01-01. 
select * from employees where hire_date>='2024-01-01';

-- Q019. List active employees only. 
select * from employees where employment_status='Active';

-- Q020. Find employees whose first name begins with A. 
select * from employees where first_name like 'A%';

-- Q021. Find employees whose last name contains a. 
select * from employees where last_name like '%a%';

-- Q022. Find employees in department IDs 1, 3 or 5. 
select * from employees where department_id in (1,3,5);

-- Q023. Find employees with no manager assigned. 
select * from employees where manager_id is null;

-- Q024. List employees sorted by salary highest first. 
select * from employees order by base_salary desc;

-- Q025. Show the five highest-paid employees. 
select * from employees order by base_salary desc limit 5;

-- Q026. List projects with a NULL end_date. 
select * from projects where end_date is null;

-- Q027. Find projects with budgets above 7000000. 
select * from projects where budget>7000000;

-- Q028. Find payroll records whose payment_status is Pending. 
select * from payroll where payment_status='Pending';

-- Q029. List employees hired during calendar year 2025 using a date range. 
select * from employees where hire_date between '2025-01-01' and '2025-12-31';

-- Q030. Display employee names in uppercase. 
select upper(concat(first_name,' ',last_name)) as employee_name from employees;

-- Q031. Show the length of each employee first name. 
select first_name, length(first_name) as name_length from employees;

-- Q032. Show each employee hire year using YEAR(). 
select employee_id, first_name, last_name, year(hire_date) as hire_year from employees;

-- Q033. Display salaries rounded to the nearest thousand. 
select round(base_salary,0) as rounded_salary from employees;

-- Q034. Show employees whose designation is Analyst or Associate. 
select * from employees where designation in ('Analyst','Associate');

-- Q035. Show active employees ordered by department and salary descending. 
select * from employees where employment_status='Active' order by department_id, base_salary desc;

-- Q036. Count all employees. 
select count(*) as total_employees from employees;

-- Q037. Count active and inactive employees separately. 
select employment_status, count(employment_status) from employees group by employment_status;

-- Q038. Find minimum, maximum and average base salary. 
select min(base_salary), max(base_salary), avg(base_salary) from employees;

-- Q039. Calculate the total monthly base salary of all employees. 
select sum(base_salary) as total_salary from employees;

-- Q040. Count employees in each department_id. 
select department_id, count(employee_id) from employees group by department_id;

-- Q041. Find average base salary by department_id. 
select department_id, round(avg(base_salary),2) from employees group by department_id;

-- Q042. Find highest base salary in each department_id. 
select department_id, max(base_salary) from employees group by department_id;

-- Q043. Find departments with more than four employees using HAVING. 
select department_id, count(employee_id) as employee_count from employees group by department_id having employee_count>4;

-- Q044. Find departments whose average salary exceeds 80000. 
select department_id, round(avg(base_salary),2) as avg_salary from employees group by department_id having avg_salary>80000;

-- Q045. Count employees by designation. 
select designation, count(employee_id) as employee_count from employees group by designation;

-- Q046. Find designations with at least three employees. 
select designation, count(employee_id) as employee_count from employees group by designation having employee_count>=3;

-- Q047. Calculate total net payroll for each pay_month. 
select pay_month, sum(net_pay) as total_net_payroll from payroll group by pay_month;

-- Q048. Calculate total bonus paid for each pay_month. 
select pay_month, sum(bonus) as total_bonus from payroll group by pay_month;

-- Q049. Find payroll months with total deductions above 200000. 
select pay_month, sum(deductions) as total_deductions from payroll group by pay_month having total_deductions> 200000;

-- Q050. Count Paid versus Pending payroll rows by month. 
select pay_month, payment_status, count(payment_status) as count_paid_pending from payroll group by pay_month, payment_status;

-- Q051. Find the average budget of Active projects. 
select project_status, avg(budget) as avg_budget from projects group by project_status having project_status='Active';

-- Q052. Count projects by project_status. 
select project_status, count(project_id) as project_count from projects group by project_status;

-- Q053. Find project statuses with more than one project. 
select project_status, count(project_id) as project_count from projects group by project_status having project_count>1;

-- Q054. Calculate total project budget by project_type. 
select project_type, sum(budget) as total_project_budget from projects group by project_type;

-- Q055. Find departments where the maximum employee salary exceeds 120000. 
select department_id, max(base_salary) as max_salary from employees group by department_id having max_salary>120000;

-- Q056. INNER JOIN Employees and Departments to show employee full name and department name. 
select concat(e.first_name,' ',e.last_name) as full_name, d.department_name from employees e
inner join departments d
on e.department_id=d.department_id;

-- Q057. Show employee name, designation and department location using a two-table join. 
select concat(e.first_name,' ',e.last_name) as full_name, e.designation, d.location from employees e
inner join departments d
on e.department_id=d.department_id;

-- Q058. List all employees in the Technology department using a join. 
select e.employee_id, e.first_name, e.last_name, d.department_name from employees e
inner join departments d
on e.department_id=d.department_id
where d.department_name='Technology';

-- Q059. Show employee name, department name and base salary, ordered by salary. 
select concat(e.first_name,' ',e.last_name) as employee_name, d.department_name, e.base_salary from employees e
inner join departments d
on e.department_id=d.department_id
order by e.base_salary desc;

-- Q060. Count employees per department using Employees JOIN Departments. 
select d.department_name, count(e.employee_id) as employee_count from employees e
inner join departments d
on e.department_id=d.department_id
group by d.department_name;

-- Q061. Show department name and average employee salary using JOIN and GROUP BY. 
select d.department_name, round(avg(e.base_salary)) as avg_salary from departments d
inner join employees e
on d.department_id=e.department_id
group by d.department_name;


-- Q062. Find department names with at least five employees using JOIN, GROUP BY and HAVING. 
select d.department_name, count(e.employee_id) as employee_count from departments d
inner join employees e
on d.department_id=e.department_id
group by d.department_name
having employee_count>=5;

-- Q063. JOIN Employees and Payroll to show employee name, pay_month and net_pay. 
select concat(e.first_name,' ',e.last_name) as employee_name, p.pay_month, p.net_pay from employees e
inner join payroll p
on e.employee_id=p.employee_id;

-- Q064. Find employees whose October 2026 payroll is Pending using two tables. 
select concat(e.first_name,' ',e.last_name) as employee_name, p.payment_status from employees e
inner join payroll p
on e.employee_id=p.employee_id
where p.pay_month like'2026-10%' and p.payment_status='Pending';

-- Q065. Show employee names and bonuses for September 2026. 
select concat(e.first_name,' ',e.last_name) as employee_name, p.pay_month, p.bonus from employees e
inner join payroll p
on e.employee_id=p.employee_id
where p.pay_month like '2026-09%';

-- Q066. Find total net_pay for each employee across three months using Employees and Payroll. 
select e.employee_id, concat(e.first_name,' ',e.last_name) as employee_name, sum(p.net_pay) as total_net_pay from employees e
inner join payroll p
on e.employee_id=p.employee_id
group by e.employee_id, employee_name;

-- Q067. Show the five employees with the highest total net_pay across all months. 
select e.employee_id, concat(e.first_name,' ',e.last_name) as employee_name, sum(p.net_pay) as total_net_pay from employees e
inner join payroll p
on e.employee_id=p.employee_id
group by e.employee_id, employee_name
order by total_net_pay desc
limit 5;

-- Q068. JOIN EmployeeProjects and Projects to show project names and assignment roles. 
select ep.project_id,p.project_name, ep.role_on_project from employeeprojects ep
inner join projects p
on ep.project_id=p.project_id;

-- Q069. JOIN Employees and EmployeeProjects to list employees and their allocation percentages. 
select * from employeeprojects;
select * from employees;
select e.employee_id, concat(e.first_name,' ',e.last_name) as employee_name, ep.allocation_pct from employees e
inner join employeeprojects ep
on e.employee_id=ep.employee_id;

-- Q070. Count assigned employees per project using Projects and EmployeeProjects. 

