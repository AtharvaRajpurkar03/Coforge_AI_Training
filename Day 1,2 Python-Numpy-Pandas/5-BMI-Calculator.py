weight=float(input("Enter the weight: "))
height=float(input("Enter the height: "))
bmi=weight/(height*2)
if bmi>=30:
    print(f"Obese for {height} height")
elif bmi<=29.9 and bmi>25:
    print(f"Over Weight for {height} height")
elif bmi<=24.9 and bmi>18.5:
    print(f"Normal for {height} height")
else:
    print("Under Weight")

