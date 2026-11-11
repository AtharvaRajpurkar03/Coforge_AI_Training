from models.inventoryproduct_model import InventoryProduct
from sqlalchemy.orm import Session
from sqlalchemy import select,func

def create_product(db:Session,data):
    product=InventoryProduct(**data.model_dump())

    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db:Session,skip:int,limit:int):
    query= select(InventoryProduct).offset(skip).limit(limit)
    result=db.scalars(query)
    return result.all()

def get_product_by_id(db:Session,product_id:int):
    return db.get(InventoryProduct,product_id)

def update_product(db:Session,product_id:int,data):
    product=db.get(InventoryProduct,product_id)

    if not product:
        return None

    for key,value in data.model_dump().items():
        setattr(product,key,value)

    db.commit()
    db.refresh(product)
    return product

def delete_product(db:Session,product_id:int):
    product=db.get(InventoryProduct,product_id)

    if not product:
        return None

    db.delete(product)
    db.commit()
    return True

def category_products(db:Session,category:str):
    query=select(InventoryProduct).where(InventoryProduct.category==category)
    result=db.scalars(query)
    return result.all()

def low_stock_products(db:Session):
    query=select(InventoryProduct).where(InventoryProduct.quantity_in_stock<=InventoryProduct.reorder_level)
    result=db.scalars(query)
    return result.all()

def increase_stock(db:Session,product_id:int, quantity:int):
    product=db.get(InventoryProduct,product_id)

    if not product:
        return None

    product.quantity_in_stock+=quantity
    db.commit()
    db.refresh(product)
    return product

def decrease_stock(db:Session,product_id:int,quantity:int):
    product=db.get(InventoryProduct,product_id)

    if not product:
        return None

    if quantity>product.quantity_in_stock:
        return "Insufficient quantity"

    product.quantity_in_stock-=quantity
    db.commit()
    db.refresh(product)
    return product
#***************************************
def total_inventory_value(db:Session):
    query=select(InventoryProduct)
    result=db.scalars(query)
    products=result.all()

    total_value=0

    for product in products:
        total_value+=(float(product.unit_price)*product.quantity_in_stock)

    return {
        "total_inventory_value":round(total_value,2)
    }


"""def inventory_value_by_category(db:Session):
    query=select(InventoryProduct)
    result=db.scalars(query)
    products=result.all()

    category_values={} """

    
    

