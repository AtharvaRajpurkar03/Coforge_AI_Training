import pandas as pd
import numpy as np

#create pandas series
#Series is One dimensional
salary_series=pd.Series([
    65000,58000,72000,80000,85000,68000,90000,67000
])
print("===========salary_series===========")
print(salary_series)

print("=============Defining Properties============")
#check properties:
print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)

#series with custom index
employee_series=pd.Series(
    [
        "Atharva","Shiv","Sahil","Prince",
        "Akash","Shreyansh","Pranjali","Hitesh"
    ],
    index=[
        "E101","E102","E103","E104",
        "E105","E106","E107","E108"
    ]
)
print("=========Series with Custom Index=========")
print(employee_series)

#Retrieve Employees:
print("========Employee Name with E103=========")
print(employee_series["E103"])
print("========Employee Name with E106=========")
print(employee_series["E106"])

