compute_hours=int(input("Enter number of compute hours: "))
storage_used=int(input("Enter storage used: "))
support_plan = input("Enter support plan (Basic/Premium/Enterprise): ")

#Assumptions
if support_plan == "Basic":
    compute_cost = compute_hours * 10
    storage_cost = storage_used * 2
    support_fee = 500

elif support_plan == "Premium":
    compute_cost = compute_hours * 8
    storage_cost = storage_used * 2
    support_fee = 1000

elif support_plan == "Enterprise":
    compute_cost = compute_hours * 6
    storage_cost = storage_used * 1
    support_fee = 2000

else:
    print("Invalid Plan")
    exit()

total_bill = compute_cost + storage_cost + support_fee

print("======== BILL DETAILS =========")
print("Compute Cost: ", compute_cost)
print("Storage Cost: ", storage_cost)
print("Support Fee: ", support_fee)
print("Final Bill: ", total_bill)