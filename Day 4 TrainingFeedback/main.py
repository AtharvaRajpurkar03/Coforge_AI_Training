from fastapi import FastAPI
from services import employee_service as service
from schemas.employee_schema import EmployeeResponse,EmployeeCreate
from config.database import Base,SessionLocal,engine

app=FastAPI(
    title="FastAPI running",
    version="1.0.1"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
        "message": "FastAPI is returning"
    }

@app.get("/employees",response_model=list[EmployeeResponse])
def getAllEmployees():
    db=SessionLocal()
    return service.get_all_employees(db)

@app.get("/employees/{employee_id}",response_model=EmployeeResponse)
def getEmployeesById(employee_id:int):
    db=SessionLocal()
    return service.get_employee_by_id(db,employee_id)

@app.post("/employees",response_model=EmployeeResponse,status_code=201)
def add(Employee):
    db=SessionLocal()
    return service.add_employee(db,Employee)