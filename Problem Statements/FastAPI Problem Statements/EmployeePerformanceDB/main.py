from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from config.database import Base,SessionLocal,engine
from config.logger import logger
from schemas.employeeperformance_schema import EmployeeCreate,EmployeeResponse,EmployeeUpdate
from services import employeeperformance_service as service

app=FastAPI(
    title="Employee Performance API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"Employee Performance Management API"
    }

@app.post("/employees",response_model=EmployeeResponse,status_code=201)
def create_employee(employee: EmployeeCreate):
    db=SessionLocal()

    try:
        new_employee=service.create_employee(db,employee)
        logger.info(f"Employee created {new_employee.employee_id}")
        return new_employee
    except IntegrityError:
        db.rollback()
        logger.warning("Duplicate employee id attempted")
        raise HTTPException(status_code=409,detail="Employee ID already exists")
    except Exception:
        logger.exception("Unexpected error during create")
        raise HTTPException(status_code=500,detail="Internal Server Error")
    finally:
        db.close()

@app.get("/employees",response_model=list[EmployeeResponse])
def get_all_employees(skip:int=0, limit:int=10):
    db=SessionLocal()

    return service.get_all_employees(db,skip,limit)

@app.get("/employees/{employee_id}",response_model=EmployeeResponse)
def get_employee_by_id(employee_id:int):
    db=SessionLocal()

    employee=service.get_employee_by_id(db,employee_id)

    if not employee:
        logger.warning(f"Employee {employee_id} not found")
        raise HTTPException(status_code=404,detail="Employee Not Found")

    return employee

@app.put("/employees/{employee_id}",response_model=EmployeeResponse)
def update_employee(employee_id:int,data:EmployeeUpdate):
    db=SessionLocal()

    try:
        employee=service.update_employee(db,employee_id,data)

        if not employee:
            logger.warning(f"Employee {employee_id} not found")
            raise HTTPException(status_code=404,detail="Employee Not Found")
        
        logger.info(f"Employee updated {employee_id}")
        return employee

    except HTTPException:
        raise

    except Exception:
        logger.exception("Update operation failed")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id:int):
    db=SessionLocal()

    employee=service.delete_employee(db,employee_id)

    if not employee:
        logger.warning(f"Employee {employee_id} not found")
        raise HTTPException(status_code=404,detail="Employee not found")

    logger.info(f"Employee deleted {employee_id}")

    return{
        "message":"Employee deleted successfully"
    }

@app.get("/department/{department}")
def filter_department(department:str):
    db=SessionLocal()

    return service.get_department_employee(db,department)

@app.get("/top-performers")
def top_performers():
    db=SessionLocal()

    return service.get_top_rated_employees(db)

@app.get("/average-rating-by-department")
def avg_dept_rating():
    db=SessionLocal()

    data=service.average_rating_by_department(db)

    return[
        {
            "department":d,
            "average_rating":round(r,2)
        }
        for d,r in data
    ]

@app.get("/highest-rated")
def highest_rated():
    db=SessionLocal()

    return service.highest_rated_employees(db)

@app.get("/classification")
def classification():
    db=SessionLocal()

    return service.employee_classification(db)




