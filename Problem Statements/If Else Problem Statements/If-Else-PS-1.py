emp_rating=int(input("Enter Employee Rating: "))
emp_experience=int(input("Enter Employee's years of experience: "))
project_delivery_status=input("Enter project delivery status: ")

if emp_rating==5 and emp_experience>10 and project_delivery_status=="on time":
    print("Give 30 percent of bonus")
elif emp_rating==4 and emp_experience>7:
    print("Give 20 percent of bonus")
elif emp_rating==3 and project_delivery_status=="delayed":
    print("Give 5 percent of bonus")
else:
    print("No bonus")