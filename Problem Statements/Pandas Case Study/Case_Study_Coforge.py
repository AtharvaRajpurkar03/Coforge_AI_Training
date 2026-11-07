import pandas as pd
import numpy as np

# 1. Load the employee CSV into a DataFrame.
employees=pd.read_csv("C:\\Users\\Atharva.Rajpurkar\\Downloads\\coforge_employees_50.csv")
projects=pd.read_csv("C:\\Users\\Atharva.Rajpurkar\\Downloads\\coforge_projects.csv")

# 2. Display the first five and last five rows.
print(employees.head())
print(employees.tail())

# 3. Show shape, column names and data types
print(employees.shape)
print(employees.columns)
print(employees.dtypes)

# 4. Run info() and describe() and explain the results. 
employees.info()
print(employees.describe())

# 5. Select EmployeeName, Department, Salary and PerformanceRating. 
selected_columns=employees[
    ["EmployeeName","Department","Salary","PerformanceRating"]
]
print(selected_columns.head())

# 6. Calculate minimum, maximum and mean salary. 
print("Minimum Salary: ",employees["Salary"].min())
print("Maximum Salary: ",employees["Salary"].max())
print("Mean Salary: ",employees["Salary"].mean())

# 7. Calculate total annual salary expenditure. 
total_salary = employees["Salary"].sum()
print("Total Salary Expenditure: ", total_salary)

# 8. Identify the youngest and oldest employees. 
youngest_employee=employees.loc[employees["Age"].idxmin()]
oldest_employee=employees.loc[employees["Age"].idxmax()]
print(youngest_employee)
print(oldest_employee)

# 9. Count employees in each department.
dept_count=employees["Department"].value_counts()
print(dept_count) 

# 10. Count employees in each office location.
loc_count=employees["Location"].value_counts()
print(loc_count)

# 11. List unique designations and their counts.
unique_designations=employees["Designation"].value_counts()
print(unique_designations)

# 12. Filter employees with Salary above INR 1,000,000.\
emp_sal=employees[employees["Salary"]>1000000]
print(emp_sal)

# 13. Filter employees with PerformanceRating >= 4. 
emp_rating=employees[employees["PerformanceRating"]>=4]
print(emp_rating)

# 14. Sort by Salary from highest to lowest. 
sorted_salary=employees.sort_values(by="Salary",ascending=False)
print(sorted_salary)

# 15. Display the five highest-paid employees.
top5=sorted_salary.head()
print(top5[
    ["EmployeeName","Salary"]
])

# 16. Find mean salary by department using groupby().
mean_salary_dept=employees.groupby("Department")["Salary"].mean()
print(mean_salary_dept)

# 17. Find minimum and maximum salary by designation.
designation_salary=employees.groupby("Designation").agg(
    Minimum_Salary=("Salary","min"),
    Maximum_Salary=("Salary","max")
).reset_index()

print(designation_salary)

# 18. Find mean performance rating by location.
loc_rating=employees.groupby("Location")["PerformanceRating"].mean()
print(loc_rating)

# 19. Count employees grouped by Department and Gender. 
emp_count=employees.groupby(
    ["Department","Gender"]
).size()

print(emp_count)

# 20. Filter employees with ExperienceYears > 5 and PerformanceRating >= 4.
experience_rating=employees[
    (employees["ExperienceYears"]>5) & 
    (employees["PerformanceRating"]>=4)
]
print(experience_rating)

# 21.  Use isin() to filter employees from any three selected locations.
selected_locations=employees[
    employees["Location"].isin(
        ["Pune","Mumbai","Noida"]
    )
]

print(selected_locations)

# 22. Create SalaryCategory (Low, Medium, High); document your thresholds.
conditions=[
    employees["Salary"]<600000,
    employees["Salary"].between(600000,1200000),
    employees["Salary"]>1200000
]

choices=[
    "Low","Medium","High"
]

employees["SalaryCategory"]=np.select(
    conditions,choices,default="Unknown"
)

print(employees["SalaryCategory"].head())

# 23. Create PerformanceCategory using clear rating thresholds. 

# 24. Calculate salary per year of experience; handle zero experience safely.

# 25. Calculate total Salary and Bonus by department. 
salary_bonus=employees.groupby("Department")[
    ["Salary","Bonus"]
].sum()

print(salary_bonus)

# 26. Calculate average TrainingHours by department. 
mean_hours_dept=employees.groupby("Department")["TrainingHours"].mean()
print(mean_hours_dept)

# 27. Identify employees with LeaveDays > 15.
emp_leave=employees[employees["LeaveDays"]>15]
print(emp_leave)

# 28. Calculate correlation between Salary and ExperienceYears.

# 29. Calculate correlation between TrainingHours and PerformanceRating.

# 30. Group by Department and Designation; show headcount and mean salary.
dept_designation=employees.groupby(
    ["Department","Designation"]
).agg(
    Headcount=("EmployeeID","count"),
    Mean_salary=("Salary","mean")
)

print(dept_designation)

# 31. Use agg() to find count, min, max, mean and median salary by department.
salary_dept=employees.groupby("Department").agg(
    SalaryCount=("Salary","count"),
    MinSalary=("Salary","min"),
    SalaryMax=("Salary","max"),
    SalaryMean=("Salary","mean"),
    SalaryMedian=("Salary","median"),
).reset_index()

print(salary_dept)

# 32. Create a pivot table of average salary by Department and Location.

# 33. Create a crosstab of Department and WorkMode. 

# 34. Convert JoiningDate to datetime and calculate tenure as of the analysis date.

# 35.  Inspect nulls and duplicates; report findings and clean only where justified.
print(employees.isnull().sum())
print(employees.duplicated().sum())

# 36.  Merge employees with projects using ProjectID.
merged=employees.merge(
    projects,
    on="ProjectID",
    how="left"
)
print(merged.head())

# 37. Compare inner, left, right and outer joins; explain row-count differences.
inner_join = employees.merge(
    projects,
    on="ProjectID",
    how="inner"
)

left_join = employees.merge(
    projects,
    on="ProjectID",
    how="left"
)

right_join = employees.merge(
    projects,
    on="ProjectID",
    how="right"
)

outer_join = employees.merge(
    projects,
    on="ProjectID",
    how="outer"
)

print(len(inner_join))
print(len(left_join))
print(len(right_join))
print(len(outer_join))

"""
============ Insights ==============
Inner: matching records only.
Left: all employees.
Right: all projects.
Outer: all records from both.
"""

# 38. Find employees on projects with ProjectBudgetINR > 10,000,000.
project_budget=merged[
    merged["ProjectBudgetINR"]>10000000
]
print(project_budget)

# 39.  Rank employees by Salary within each department.

# 40.  Find the top three highest-paid employees per department.
print("***********")
top3_dept=(employees.sort_values("Salary",ascending=False).groupby("Department").head(3))
print(top3_dept)

# 41.  Use transform() to compute Salary minus department mean Salary.

# 42.  Calculate the 25th, 50th, 75th and 90th Salary percentiles.
percentiles = employees[
    "Salary"
].quantile(
    [0.25,0.50,0.75,0.90]
)

print(percentiles)

# 43. Detect Salary outliers using the interquartile range (IQR) method.

# 44. Create a weighted performance score from PerformanceRating, TrainingHours and ProjectsCompleted; document normalization and weights. 

# 45. Create and query a MultiIndex by Department and Location. 

# 46. Analyze employee joining counts by year and quarter. 

# 47. Calculate cumulative Salary by department after sorting by Salary. 

# 48. Use apply() to flag promotion eligibility with transparent business rules. 

# 49. Build a department scorecard with named aggregation and sorting. 

# 50. Export cleaned employees, project-enriched data, department scorecard and top performers to CSV.