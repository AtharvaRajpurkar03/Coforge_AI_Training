import numpy as np

salary=np.array([65000,58000,72000,80000,85000,68000,90000,76000])
print("======== Salary ==========")
print(salary)

# Numpy Properties
print("========= Salary Operations=========")
print("Arrays: ", salary)
print("Type: ", type(salary))
print("Dimensions: ", salary.ndim)
print("Shape: ", salary.shape)
print("Size: ", salary.size)
print("Data Type: ", salary.dtype)

# 2 Dimensions because of 2 brackets
salary=np.array([[65000,58000,72000,80000,85000,68000,90000,76000]])
print("Dimensions: ", salary.ndim)

rating=np.array([4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3])
print("========= Ratings =========")
print(rating)

# Check Properties:
print("========= Ratings Properties =========")
print("Rating Shape: ", rating.shape)
print("Rating Size: ", rating.size)
print("Rating Data Type: ", rating.dtype)

# Numpy Indexing
print("========= Ratings Indexing =========")
salary=np.array([65000,58000,72000,80000,85000,68000,90000,76000])
print("First Salary: ", salary[0])
print("Third Salary: ", salary[2])
print("Last Salary: ", salary[-1])
print("Second Last Salary: ", salary[-2])
print("Third Last Salary: ", salary[-3])

#Numpy Slicing
print("========Numpy Slicing==========")
print(salary[0:3])
print(salary[-3:])
print(salary[2:])
print(salary[1:1])
print(salary[1:-1])

# Find employees earning above 75000
print("========Salary Above 75000==========")

high_salary=salary[salary>75000]
print("Employee Salary: ",high_salary)
print("Employee Count: ",len(high_salary))

# Find employee with rating above 4.5
print("========Rating Above 4.5==========")

high_rating=rating[rating>4.5]
print("Employee Salary: ",high_rating)
print("Employee Count: ",len(high_rating))

# Conditional Salary Increment
# Employees earning below 70000 get 10% increment -> 1.10
# Rest receives 5% -> 1.05

new_salary=np.where(salary<70000,salary*1.10,salary*1.05)
print("Original Salary: ", salary)
print("Updated Salary: ",new_salary)

# Employee rated 4.5 or above recieves 15% bonus.
# Other remployees receives 5%

bonus=np.where(rating>=4.5,salary*0.15,salary*0.05)
print("Employee Bonus: ",bonus)

# Salary after bonus
salaru_with_bonus=salary+bonus

print("Original Salary: ",salary)
print("Bonus: ",bonus)
print("Salary after Salary: ",salaru_with_bonus)