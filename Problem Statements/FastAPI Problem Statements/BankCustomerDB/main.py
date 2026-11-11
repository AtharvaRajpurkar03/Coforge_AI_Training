from fastapi import FastAPI,HTTPException
from sqlalchemy.exc import IntegrityError
from config.database import SessionLocal,Base,engine
from config.logger import logger
from schemas.bankcustomer_schema import BankCustomerCreate,BankCustomerResponse,BankCustomerUpdate,TransactionRequest
from services import bankcustomer_service as service

app=FastAPI(
    title="Banking Customer Account API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"Banking Customer Account API"
    }

@app.post("/accounts",response_model=BankCustomerResponse,status_code=201)
def open_account(customer:BankCustomerCreate):
    db=SessionLocal()

    try:
        new_customer=service.create_customer(db,customer)
        logger.info(f"Account Created {new_customer.account_number}")
        return new_customer

    except IntegrityError:
        db.rollback()
        logger.warning("Duplicate Email or Account Number")
        raise HTTPException(status_code=409,detail="Email or Account Number already exists")

    except Exception:
        logger.exception("Create Account Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.get("/accounts",response_model=list[BankCustomerResponse])
def get_accounts(skip:int=0,limit:int=10):
    db=SessionLocal()

    return service.get_all_customers(db,skip,limit)

@app.get("/accounts/{account_number}",response_model=BankCustomerResponse)
def get_account(account_number:str):
    db=SessionLocal()

    customer=service.get_account(db,account_number)

    if not customer:
        logger.warning(f"Account {account_number} not found")
        raise HTTPException(status_code=404,detail="Account not found")

    return customer

@app.put("/accounts/{account_number}",response_model=BankCustomerResponse)
def update_account(account_number:str,data:BankCustomerUpdate):
    db=SessionLocal()

    try:
        customer=service.update_customer(db,account_number,data)

        if not customer:
            logger.warning(f"Account {account_number} not found")
            raise HTTPException(status_code=404,detail="Account not found")

        logger.info(f"Account Updated {account_number}")
        return customer

    except HTTPException:
        raise

    except Exception:
        logger.exception("Update Error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.delete("/accounts/{account_number}")
def close_account(account_number:str):
    db=SessionLocal()

    customer=service.close_account(db,account_number)

    if not customer:
        logger.warning(f"Account {account_number} not found")
        raise HTTPException(status_code=404,detail="Account not found")

    if customer=="Balance exists":
        raise HTTPException(status_code=409,detail="Account balance must be zero")

    logger.info(f"Account Closed {account_number}")

    return {
        "message":"Account closed successfully"
    }

@app.get("/branch/{branch_name}",response_model=list[BankCustomerResponse])
def branch_accounts(branch_name:str):
    db=SessionLocal()

    return service.filter_branch(db,branch_name)

@app.get("/account-type/{account_type}",response_model=list[BankCustomerResponse])
def account_type(account_type:str):
    db=SessionLocal()

    return service.filter_account_type(db,account_type)

@app.put("/deposit/{account_number}",response_model=BankCustomerResponse)
def deposit(account_number:str,data:TransactionRequest):
    db=SessionLocal()

    customer=service.deposit_amount(db,account_number,data.amount)

    if not customer:
        logger.warning(f"Account {account_number} not found")
        raise HTTPException(status_code=404,detail="Account not found")

    if customer=="Inactive":
        raise HTTPException(status_code=409,detail="Account is inactive")

    return customer

@app.put("/withdraw/{account_number}",response_model=BankCustomerResponse)
def withdraw(account_number:str,data:TransactionRequest):
    db=SessionLocal()

    customer=service.withdraw_amount(db,account_number,data.amount)

    if not customer:
        logger.warning(f"Account {account_number} not found")
        raise HTTPException(status_code=404,detail="Account not found")

    if customer=="Inactive":
        raise HTTPException(status_code=409,detail="Account is inactive")

    if customer=="Insufficient":
        raise HTTPException(status_code=409,detail="Insufficient funds")

    return customer

@app.get("/branch-deposits")
def branch_deposit_summary():
    db = SessionLocal()

    data = service.branch_deposits(db)

    return [
        {
            "branch_name": branch,
            "total_deposit": float(total)
        }
        for branch, total in data
    ]