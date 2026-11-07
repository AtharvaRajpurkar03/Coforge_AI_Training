age=int(input("Enter customer's age: "))
smoking_habit=input("Do customer smoke? : ")
bmi=float(input("Enter BMI of customer: "))
existing_disease=input("Do customer has any existing disease? :")

if age>50 and smoking_habit=="yes":
    print("High Premium")
elif existing_disease=="yes" and age>60:
    print("Reject")
elif bmi<=29.9 and bmi>=25:
    print("Medium premium for overweight customers")
else:
    print("Low premium for healthy young customers")
