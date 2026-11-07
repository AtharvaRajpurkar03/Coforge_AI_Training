salary=int(input("Enter the Salary: "))
if salary>=50000:
    salary=salary+0.2*salary
elif salary<50000 and salary>=30000:
    salary=salary+0.1*salary
else:
    salary=salary+0.05*salary
print(salary)