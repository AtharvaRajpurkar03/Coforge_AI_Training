while True:
    amount=int(input("Purchase amount of user: "))

    if amount<0:
        print("system stopped")
        break
    if amount==0:
        continue
    if amount>1000:
        print("purchase amount: ",amount)