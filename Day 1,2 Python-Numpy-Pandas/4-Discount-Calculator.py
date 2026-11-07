amount=int(input("Enter the amount: "))
if amount>=5000:
    amount=amount-0.2*amount
elif amount<5000 and amount>=2000:
    amount=amount-0.1*amount
else:
    amount=amount-0.05*amount
print(amount)