annual_income=int(input("Enter annual income: "))
age=int(input("Enter age: "))
investment_amount=int(input("Enter amount invested: "))

if age>=60:
    print("Allow senior citizen exemption")
if annual_income<50000:
    tax=0
    print(tax)
elif annual_income<1000000 and annual_income>=500000:
    tax=0.1*annual_income
    print(tax)
elif annual_income<2000000 and annual_income>=1000000:
    tax=0.2*annual_income
    print(tax)
else:
    tax=0.3*annual_income
    print(tax)

#Example investment deduction
tax = tax - (investment_amount * 0.05)
if tax < 0:
    tax = 0
print("Tax payable:", tax)

