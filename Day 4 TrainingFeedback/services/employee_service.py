# model.dump() -> converts request object into key value pair {Dictionary}
# session.update, session.delete etc things will be used to perform operations on db
# commit is used to save the operations performed in db

from decimal import Decimal
from sqlalchemy.orm import Session
from models.employee_model import Employee
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError

# Function to add a new employee into SQL database
# db-> database session used to communicate with SQL
# data-> employee information received from FastAPI

def add_employee(db: Session, data):

    employee=Employee(**data.model_dump())

    db.add(employee) # this tells SQLAlchemy that a new employee needs to be inserted

    db.commit() # record get saved permanently in db

    db.refresh(employee) # refresh employee object from db. This recieves latest information from Mysql

    return employee


def get_all_employees(db: Session):

    # create query using sqlalchemy
    query = select(Employee).order_by(Employee.employee_id)
    result=db.scalars(query) # executes query 
    employees=result.all() 
    return employees

# search employee by id:
def get_employee_by_id(db: Session, employee_id: int):
    return db.get(Employee, employee_id)

# update employee:
def update_employee(db: Session, employee_id:int, data):
    employee=db.get(Employee, employee_id)

    if employee is None:
        return None

    for key, value in data.model_dump().items(): # .items() -> iterates
        setattr(employee,key,value) # function that sets updated value

    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise

# delete employee:
def delete_employee(db: Session, employee_id: int):
    employee=db.get(Employee, employee_id) # retrieve employee by Id

    if employee is None: # if not present, return false
        return False

    db.delete(employee) # if present, delete the record
    db.commit() # save the changes

    return True 

# search by department:

