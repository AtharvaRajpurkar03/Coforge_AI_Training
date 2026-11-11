from sqlalchemy.orm import Session
from sqlalchemy import select,func
from models.employeeperformance_model import EmployeePerformance

def create_employee(db:Session,data):
    employee=EmployeePerformance(**data.model_dump())

    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_all_employees(db:Session,skip:int,limit:int):
    query=(select(EmployeePerformance).offset(skip).limit(limit))
    result=db.scalars(query)
    return result.all()

def get_employee_by_id(db:Session,employee_id:int):
    return db.get(EmployeePerformance,employee_id)

def update_employee(db:Session,employee_id: int, data):
    employee=db.get(EmployeePerformance,employee_id)

    if employee is None:
        return None

    employee.performance_rating=data.performance_rating
    employee.attendance_percentage=data.attendance_percentage
    employee.projects_completed=data.projects_completed

    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db:Session, employee_id:int):
    employee=db.get(EmployeePerformance,employee_id)

    if employee is None:
        return None

    db.delete(employee)
    db.commit()
    return True

def get_department_employee(db:Session, department:str):
    query=select(EmployeePerformance).where(EmployeePerformance.department==department)
    result=db.scalars(query)   
    return result.all() 

def get_top_rated_employees(db:Session):
    query=select(EmployeePerformance).where(EmployeePerformance.performance_rating>=4)
    result=db.scalars(query)
    return result.all()

def average_rating_by_department(db: Session):
    query=(select(EmployeePerformance.department, func.avg(EmployeePerformance.performance_rating).label("average_rating")).group_by(EmployeePerformance.department))
    result=db.execute(query)
    return result.all()

def highest_rated_employees(db:Session):
    query=select(EmployeePerformance).order_by(EmployeePerformance.performance_rating.desc()).limit(5)
    result=db.scalars(query)
    return result.all()

def employee_classification(db:Session):
    query=select(EmployeePerformance)
    result=db.scalars(query)
    employees=result.all()

    employee_result=[]

    for emp in employees:
        if emp.performance_rating>=4.5:
            category="Outstanding"
        elif emp.performance_rating>=3.5:
            category="Good"
        else:
            category="Need Improvement"

        employee_result.append(
            {
                "employee_id":emp.employee_id,
                "employee_name":emp.employee_name,
                "classification":category
            }
        )
    return employee_result




