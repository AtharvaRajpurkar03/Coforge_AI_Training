monthly_salary=int(input("Enter monthly salary of an employee: "))
credit_score=int(input("Enter credit score: "))
existing_loan_amount=int(input("Enter existing loan amount: "))
employement_type=input("Enter employement type: ")

if monthly_salary>80000 and credit_score>750 and existing_loan_amount<20000:
    print("Approve immediately")
elif monthly_salary>50000 and credit_score>650:
    print("Approve with caution")
elif credit_score<600:
    print("Reject")
else:
    print("Require manual review")