import logging
from fastapi import FastAPI, HTTPException, status
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema
from app.crud import get_category_by_id, get_category_list
from app.db import init_db, generate_schema


log = logging.getLogger("uvicorn")

app = FastAPI()


# @app.get("/dishes/")
# def get_dish_list():
#     with get_db() as db:
#         dish_list = db.query(Dish).all()
        
#         # for dish in dish_list:
#         #     log.debug(dish)

#         return dish_list
    

# @app.get("/dishes/{dish_id}", response_model=DishSchema)
# def get_dish(dish_id: int):
#     with get_db() as db:
#         dish = db.query(Dish).filter(Dish.id == dish_id).first()
#         return dish

@app.on_event("startup")
async def startup_event():
    log.info("Stating up...")
    await generate_schema()
    init_db(app)
    
@app.get("/categories/", response_model=list[CategorySchema])
async def get_categories():
    return await get_category_list()

    
@app.get("/categories/{category_id}", response_model=CategorySchema)
async def get_category(category_id: int):
    category = await get_category_by_id(category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")
    return category