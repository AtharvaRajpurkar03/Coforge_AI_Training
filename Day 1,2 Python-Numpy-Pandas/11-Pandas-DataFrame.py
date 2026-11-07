import pandas as pd
import numpy as np

# Pandas -> It is used for data manipulation. Analyze, extract, clean, validate, tranform and load. 
# Two types of data engineering: ETL, ELT

employee_data={
    "Employee_ID":["E101","E102","E103","E104","E105","E106","E107","E108"],
    "Employee_Name":["Atharva","Shiv","Sahil","Prince","Akash","Shreyansh","Pranjali","Hitesh"],
    "Department":["Sales","HR","Sales","Finance","IT","Sales","IT","Finance"],
    "City":["Delhi","Mumbai","Pune","Delhi","Mumbai","Bengaluru","Pune","Delhi"],
    "Salary":[65000,58000,72000,80000,85000,68000,90000,76000],
    "Experience":[5,4,7,8,6,5,9,6],
    "Rating":[4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3]
}

#DataFrame -> Two Dimensional -> Rows and Columns

print("=========Create Employee Dataframe==========")
employees_df=pd.DataFrame(employee_data)
print(employee_data)

#Inspect Dataframe
print("========Dataframe Shapes========")
print(employees_df.shape)
print(employees_df.columns)
print(employees_df.dtypes)

print("=======================")

# Head()
print(employees_df.head())

print("=======================")

#First Three Rows
print(employees_df.head(3)) 

print("=======================")

# Tail()
print(employees_df.tail())

print("=======================")

#Last Two Rows
print(employees_df.tail(2))

print("=========DESCRIBE==============")
employees_df.info()
print(employees_df.describe())

# Select One Column
print("======Select One Column========")
print(employees_df["Employee_Name"])

#Select Multiple Column
print("=========Select Multiple Column=========")
print(employees_df[["Employee_Name","Salary"]])

#print(employees_df["Employee_Name","Salary"])

#Employee salary greater than 80000
emp_sal_result=employees_df[employees_df["Salary"]>80000]
print(emp_sal_result)

#Rating > 4.5
emp_rating_result=employees_df[employees_df["Rating"]>4.5]
print(emp_rating_result)

#Department = Sales
emp_dept_sales_result=employees_df[employees_df["Department"]=="Sales"]
print(emp_dept_sales_result)

#City = Delhi
emp_city_delhi_result=employees_df[employees_df["City"]=="Delhi"]
print(emp_city_delhi_result)

print("*************************")
#multiple conditions: Rating>=4.5 and Salary>=70000
emp_rating_salary_result=employees_df[
    (employees_df["Rating"]>=4.5) &
    (employees_df["Salary"]>70000)
    ]
print(emp_rating_salary_result)

print("************************")
# Department == IT or Finance
emp_dept_IT_Finance_result=employees_df[
    (employees_df["Department"]=="IT") |
    (employees_df["Department"]=="Finance")
]
print(emp_dept_IT_Finance_result)

print("************************")
# Important -> to check whether data is present in df using isin
emp_dept_IT_Finance_result1=employees_df[
    employees_df["Department"].isin(["IT","Finance"])
]
print(emp_dept_IT_Finance_result1)

print("************************")
# Creating new column -> Salary * 12
employees_df["Annual Salary"]=employees_df["Salary"]*12
print(employees_df)

print("************************")
# Increment in salary with 8%
employees_df["Revised Salary"]=employees_df["Salary"]+employees_df["Salary"]*0.08
print(employees_df)

# bonus of 0.05
employees_df["Bonus"]=employees_df["Revised Salary"]*0.05
print(employees_df)

print("************************")
# salary + performance bonus 
employees_df["Monthly Compensation"]=employees_df["Bonus"]+employees_df["Revised Salary"]
print(employees_df)

print("************************")
# mean, max, min, sum
mean_salary=employees_df["Salary"].mean()
print("Mean Salary: ",mean_salary)

max_salary=employees_df["Salary"].max()
print("Max Salary: ",max_salary)

min_salary=employees_df["Salary"].min()
print("Min Salary: ",min_salary)

sum_salary=employees_df["Salary"].sum()
print("Sum of Salary: ",sum_salary)

# mean of Rating
mean_rating=employees_df["Rating"].mean()
print("Mean Rating: ",mean_rating)

#Count of Depatment -> values_count
dept_count=employees_df["Department"].value_counts()
print(dept_count)

# total count of dept -> len() on df
dept_len=len(employees_df["Department"].value_counts())
print(dept_len)

# nuniqnue()
dept_unique=employees_df["Department"].nunique()
print(dept_unique)

# sort_values() 
salary_sort=employees_df.sort_values(by="Salary")
print(salary_sort)

# sort_values() -> sorting in descending values
salary_sort=employees_df.sort_values(by="Salary",ascending=False)
print(salary_sort)

# top 3 highest paid employees
top_3_highest_salary=employees_df.sort_values(by="Salary",ascending=False).head(3)
print(top_3_highest_salary)

