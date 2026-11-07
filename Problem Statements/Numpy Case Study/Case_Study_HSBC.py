import pandas as pd
import numpy as np

# 21. Read the supplied CSV using pd.read_csv
hsbc_df=pd.read_csv("C:\\Users\\Atharva.Rajpurkar\\Downloads\\HSBC_Synthetic_Banking_Customers.csv")

# 22. Display first and last ten rows
print(hsbc_df.head(10))
print(hsbc_df.tail(10))

# 23. Inspect shape, columns, dtypes and info().
print(hsbc_df.shape)

print(hsbc_df.columns)

print(hsbc_df.size) 

print(hsbc_df.dtypes)

hsbc_df.info()

# 24. Generate numerical descriptive statistics using describe().
print(hsbc_df.describe)

# 25. Check missing values and duplicate Customer_ID values.
print(hsbc_df.isnull().sum())

print(hsbc_df.duplicated().sum())

duplicate_ids=hsbc_df["Customer_ID"].duplicated().sum()
print(duplicate_ids)

# 1. Convert Account_Balance into a NumPy array
account_balance=hsbc_df["Account_Balance"].to_numpy()
print(account_balance)

# 2. Inspect array ndim, shape, size and dtype
print(account_balance.ndim)  
print(account_balance.shape) 
print(account_balance.size) 
print(account_balance.dtype) 

# 3. Calculate minimum and maximum balances
print("Max Balance: ",account_balance.max()) 
print("Min Balance: ",account_balance.min()) 

# 4. Calculate sum, mean, median and standard deviation of balances
print("=========== Balance Statistics ==========")
print(account_balance.sum())
print(account_balance.mean())
# print(account_balance.median())  #####################
print(account_balance.std())

# 5. Find the 25th, 50th and 75th balance percentiles
print("=========== Percentiles ==========")
print("25th: ", np.percentile(account_balance, 25))
print("50th: ", np.percentile(account_balance, 50))
print("75th: ", np.percentile(account_balance, 75))

#6. Filter balances above INR 500,000
print("=========== Balance above 500000 ==========")
account_balance_result=account_balance[account_balance>500000]
print(account_balance_result)

# 7. Identify credit scores below 650 using boolean masking
print("=========== Credit Score below 650 ==========")
credit_score=hsbc_df["Credit_Score"].to_numpy()
# print(credit_score)

low_credit_score=credit_score[credit_score<650]
print(low_credit_score)

# 8. Sort balances ascending and descending
print("=========== Balances in Ascending and Descending Order ==========")
ascending_account_balance=np.sort(account_balance)
print("Ascending: ",ascending_account_balance)
ascending_account_balance=np.sort(account_balance)[::-1]
print("Ascending: ",ascending_account_balance)

# 9. Compute total monthly deposits and total monthly withdrawals.
print("=====================")
monthly_deposits=hsbc_df["Monthly_Deposit"].to_numpy()
monthly_withdrawals=hsbc_df["Monthly_Withdrawal"].to_numpy()

total_monthly_deposits=monthly_deposits.sum()
print("Total Monthly Deposits: ",total_monthly_deposits)

total_monthly_withdrawals=monthly_withdrawals.sum()
print("Total Monthly Withdrawals: ",total_monthly_withdrawals)

# 10. Use vectorization to calculate hypothetical balances after a 5% increase
revised_balance=account_balance*1.05
print("Account balance after 5% Increase: ",revised_balance)

# 11. Use np.where to classify balances as High (> INR 500,000) or Low
print("=========== Balance Type If Balance > 500000 ==========")
balance_type=np.where(account_balance>500000,"High","Low")
hsbc_df["Balance_Type"]=balance_type
print(hsbc_df["Balance_Type"].head())

# 12. Use np.select to categorize balances into Low (< INR 100,000), Medium (INR 100,000–500,000) and High (> INR 500,000).
print("=========== Balance Category ==========")

conditions=[
    account_balance<100000,
    (account_balance<=500000) & (account_balance>=100000),
    account_balance>500000
]

balance_choice=[
    "Low","Medium","High"
]

hsbc_df["Balance Category"]=np.select(
    conditions,balance_choice,default="Unknown"
)

print(hsbc_df["Balance Category"].head())

# 13. Compute deposit-to-income ratio; handle zero income safely.


# 14. Identify records where monthly withdrawals exceed monthly deposits
print("=========== Records With Monthly Withdrawals Exceed Monthly Deposits ==========")

excess_withdrawals=hsbc_df[hsbc_df["Monthly_Withdrawal"]>hsbc_df["Monthly_Deposit"]]
print(excess_withdrawals)

# 15. Use np.unique to summarize credit-score frequencies

# 16. Use np.argsort to locate the five largest balances.
print("=========== Located Five Largest Balances ==========")

top_5_balances=np.argsort(account_balance)[-5:]
#print(top_5_balances)
print(hsbc_df.iloc[top_5_balances])

# 17. Perform min-max normalization of balances; handle constant arrays safely.

# 18. Compute z-scores for balances; handle zero standard deviation safely.

# 19. Build a 2D array with balance, deposit and withdrawal columns and inspect axis-wise totals

# 20. Calculate Pearson correlation between income and account balance.

# 26. Select customer name, city, balance and credit score columns
print("=========== Selected Columns ==========")

selected_columns=hsbc_df[
    ["Customer_Name","City","Account_Balance","Credit_Score"]
]

print(selected_columns.head())

# 27. Filter customers aged 25 through 40 inclusive
print("=========== Customers with age 25 to 40 ==========")

customer_age_25_40=hsbc_df[
    hsbc_df["Age"].between(25,40)
]

print(customer_age_25_40)

# 28. Find active Savings accounts
print("=========== Active Saving Accounts ==========")

active_saving_accounts=hsbc_df[
    (hsbc_df["Account_Status"]=="Active") &
    (hsbc_df["Account_Type"]=="Savings")
]

print(active_saving_accounts)

# 29. Sort by balance and monthly income, descending
print("=========== Descending Balance and Monthly Income ==========")

sorted_customers=hsbc_df.sort_values(by=["Account_Balance","Monthly_Income"],ascending=False)
print(sorted_customers.head())

# 30. Create Net_Monthly_Flow = Monthly_Deposit - Monthly_Withdrawal
print("=========== Net Monthly Flow ==========")

hsbc_df["Net_Monthly_Flow"]=hsbc_df["Monthly_Deposit"]-hsbc_df["Monthly_Withdrawal"]
print(hsbc_df["Net_Monthly_Flow"].head())

# 31. Group by City and calculate total Account_Balance.
print("=========== Total Balance Group By City ==========")

city_total_balance=hsbc_df.groupby("City")["Account_Balance"].sum()
print(city_total_balance)

# 32. Group by Account_Type and calculate average Monthly_Income.
print("=========== Total Monthly Income Group By Account Type ==========")

account_type_total_monthly_income=hsbc_df.groupby("Account_Type")["Monthly_Income"].mean()
print(account_type_total_monthly_income)

# 33. Compute branch-wise deposit and withdrawal totals.
print("=========== Branch Wise Total Deposit and Withdrawal ==========")

total_deposit_withdrawal_by_branch=hsbc_df.groupby("Branch")[
    ["Monthly_Deposit","Monthly_Withdrawal"]
].sum()

print(total_deposit_withdrawal_by_branch)

# 34. Use agg to report minimum, maximum, mean and median balances by branch.
print("=========== Agg Min, Max, Mean, Median Balances by Branch ==========")

branch_balance_statistics=hsbc_df.groupby("Branch").agg(
    min_balance=("Account_Balance","min"),
    max_balance=("Account_Balance","max"),
    mean_balance=("Account_Balance","mean"),
    median_balance=("Account_Balance","median"),
).reset_index()

print(branch_balance_statistics)

# 35. 35. Create a pivot table of total balance by City and Account_Type.

# 36. Use pd.cut to create age groups: 18–25, 26–40, 41–60 and 61+.

# 37. Use groupby().transform() to calculate each customer’s balance minus branch average.

# 38. Create a separate Branch_Details DataFrame with Branch and Region; merge it on Branch and validate the join.

# 39. Find the top three customers by balance within each City.
print("=========== Top 3 Customers by Balance within City ==========")

top_3_customers=hsbc_df.sort_values(by="Account_Balance",ascending=False).groupby("City").head(3)
print(top_3_customers[
    ["City","Customer_Name","Account_Balance"]
])

# 40. Create a branch summary with total balance, mean credit score, counts by account status and total net monthly flow.
print("=========== Branch Summary ==========")

branch_summary=hsbc_df.groupby("Branch").agg(
    Total_Balances=("Account_Balance","sum"),
    Mean_Credit_Score=("Credit_Score","mean"),
    Count_Account_status=("Account_Status","count"),
    Total_Net_Flow=("Net_Monthly_Flow","sum")
).reset_index()

print(branch_summary)