from pydantic import Field,BaseModel,ConfigDict
from decimal import Decimal

class InventoryProductBase(BaseModel):
    product_name: str=Field(min_length=2)
    category: str=Field(min_length=2)
    supplier_name: str=Field(min_length=2)
    unit_price: Decimal=Field(gt=0)
    quantity_in_stock: int=Field(ge=0)
    reorder_level: int=Field(ge=0)
    warehouse_location: str=Field(min_length=2)
    is_active: bool

class InventoryProductCreate(InventoryProductBase):
    pass

class InventoryProductResponse(InventoryProductBase):
    product_id: int
    model_config=ConfigDict(from_attributes=True)

class InventoryProductUpdate(BaseModel):
    product_name: str=Field(min_length=2)
    category: str=Field(min_length=2)
    supplier_name: str=Field(min_length=2)
    unit_price: Decimal=Field(gt=0)
    reorder_level: int=Field(ge=0)
    warehouse_location: str=Field(min_length=2)
    is_active: bool

class StockAdjustment(BaseModel):
    quantity_in_stock: int=Field(gt=0)



