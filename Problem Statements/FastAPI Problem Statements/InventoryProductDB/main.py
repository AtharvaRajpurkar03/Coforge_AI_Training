from fastapi import FastAPI,HTTPException
from config.database import Base,engine,SessionLocal
from config.logger import logger
from schemas.inventoryproduct_schema import InventoryProductCreate,InventoryProductResponse,InventoryProductUpdate,StockAdjustment
from services import inventoryproduct_service as service
from sqlalchemy.exc import IntegrityError

app=FastAPI(
    title="Inventory Product Management API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
        "message":"Inventory Product Management API"
    }

@app.post("/products",response_model=InventoryProductResponse,status_code=201)
def add_product(product:InventoryProductCreate):
    db=SessionLocal()

    try:
        new_product=service.create_product(db,product)
        logger.info(f"Product created {new_product.product_id}")
        return new_product

    except IntegrityError:
        db.rollback()
        logger.warning("Duplicate product ID")
        raise HTTPException(status_code=409,detail="Product ID already exist")

    except Exception:
        logger.exception("Create error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.get("/products",response_model=list[InventoryProductResponse])
def get_all_products(skip:int =0, limit:int=10):
    db=SessionLocal()

    return service.get_all_products(db,skip,limit)

@app.get("/products/{product_id}",response_model=InventoryProductResponse)
def get_products_by_id(product_id:int):
    db=SessionLocal()

    product=service.get_product_by_id(db,product_id)

    if not product:
        logger.warning(f"Product {product_id} not found")
        raise HTTPException(status_code=404,detail="Product not found")

    return product

@app.put("/products/{product_id}",response_model=InventoryProductResponse)
def update_product(product_id:int,data:InventoryProductUpdate):
    db=SessionLocal()

    try:
        product=service.update_product(db,product_id,data)

        if not product:
            logger.warning(f"Product {product_id} not found")
            raise HTTPException(status_code=404,detail="Product not found")

        logger.info(f"Product {product_id} updated")
        return product

    except HTTPException:
        raise

    except Exception:
        logger.exception("Update error")
        raise HTTPException(status_code=500,detail="Internal Server Error")

    finally:
        db.close()

@app.delete("/product/{product_id}")
def delete_product(product_id:int):
    db=SessionLocal()

    product=service.delete_product(db,product_id)

    if not product:
        logger.warning(f"Product {product_id} not found")
        raise HTTPException(status_code=404,detail="Product not found")

    logger.info(f"Product {product_id} deleted")

    return {
        "message":"Product deleted successfully"
    }

@app.get("/category/{category}",response_model=list[InventoryProductResponse])
def category_products(category:str):
    db=SessionLocal()

    return service.category_products(db,category)

@app.get("/low-stocks",response_model=list[InventoryProductResponse])
def low_stocks():
    db=SessionLocal()

    return service.low_stock_products(db)

@app.put("/increase-stock/{product_id}",response_model=InventoryProductResponse)
def increase_stocks(product_id:int,data:StockAdjustment):
    db=SessionLocal()

    product = service.increase_stock(db,product_id,data.quantity_in_stock)

    if not product:
        logger.warning(f"Product {product_id} not found")
        raise HTTPException(status_code=404,detail="Product not found")

    logger.info(f"Product {product_id} stock increased")

    return product

@app.put("/decrease-stock/{product_id}",response_model=InventoryProductResponse)
def decrease_stocks(product_id:int,data:StockAdjustment):
    db=SessionLocal()

    product = service.decrease_stock(db,product_id,data.quantity_in_stock)

    if not product:
        logger.warning(f"Product {product_id} not found")
        raise HTTPException(status_code=404,detail="Product not found")

    if product == "Insufficient quantity":
        raise HTTPException(status_code=409,detail="Insufficient stock")
    
    logger.info(f"Product {product_id} stock increased")

    return product

@app.get("/inventory-value")
def inventory_value():
    db = SessionLocal()

    return service.total_inventory_value(db)

'''@app.get("/inventory-value-by-category")
def inventory_value_category():
    db = SessionLocal()

    return service.inventory_value_by_category(db)'''
    





