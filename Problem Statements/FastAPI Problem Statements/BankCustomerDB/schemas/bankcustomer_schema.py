from pydantic import BaseModel,Field,EmailStr,ConfigDict
from decimal import Decimal
from datetime import date

class BankCustomerBase(BaseModel):
    
    customer_name: str = Field(min_length=2)
    email: EmailStr
    account_number: str
    account_type: str = Field(pattern="^(Savings|Current)$")
    branch_name: str = Field(min_length=2)
    balance: Decimal = Field(ge=0)
    is_active: bool
    opened_on: date


class BankCustomerCreate(BankCustomerBase):
    pass

class BankCustomerResponse(BankCustomerBase):
    customer_id: int
    model_config = ConfigDict(from_attributes=True)

class BankCustomerUpdate(BaseModel):
    email: EmailStr
    branch_name: str = Field(min_length=2)

class TransactionRequest(BaseModel):
    amount: Decimal = Field(gt=0)