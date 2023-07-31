import logging
from fastapi import FastAPI, HTTPException, status
from app.schemas import (
    UserSchema,
    DishSchema,
    DishUpdateSchema,
    OrderSchema,
    CategorySchema,
    CategoryCreateSchema,
    DishCreateSchema,
    OrderWithDishSchema,
)
from app.crud import (
    get_category_by_id,
    get_category_list,
    create_category,
    get_dish_list,
    create_dish,
    get_dish_by_id,
    update_dish,
    get_order_list,
    get_order_by_id,
    get_orders_by_user_id,
    get_orders_by_user_email,
    get_dishes_by_order_id,
    get_orders_by_dish_id,
)
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


@app.get("/categories/{category_id}/", response_model=CategorySchema)
async def get_category(category_id: int):
    category = await get_category_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found",
        )
    return category


@app.post("/categories/", response_model=CategorySchema)
async def create_category_(category_schema: CategoryCreateSchema):
    category = await create_category(category_schema.name)
    return category


@app.get("/dishes/", response_model=list[DishSchema])
async def get_dish_list_(category_id: int | None = None):
    dish_list = await get_dish_list(category_id)
    return dish_list


@app.post("/dishes/", response_model=DishSchema)
async def create_dish_(dish_schema: DishCreateSchema):
    new_dish = await create_dish(dish_schema)
    return new_dish


@app.put("/dishes/", response_model=DishSchema)
async def update_dish_(dish_schema: DishUpdateSchema):
    dish = await update_dish(dish_schema)
    return dish


@app.get("/dishes/{dish_id}/", response_model=DishSchema)
async def get_dish_(dish_id: int):
    dish = await get_dish_by_id(dish_id)
    if dish is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish with id {dish_id} not found",
        )
    return dish


@app.get("/orders/", response_model=list[OrderWithDishSchema])
async def get_orders():
    order_list = await get_order_list()
    return order_list


@app.get("/orders/{order_id}/", response_model=OrderSchema)
async def get_order(order_id: int):
    order = await get_order_by_id(order_id)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Order with id {order_id} not found",
        )
    return order

@app.get("/orders/from-user/{user_id}/", response_model=list[OrderSchema])
async def get_orders_by_user_id_(user_id: int): 
    return await get_orders_by_user_id(user_id) 


@app.get("/orders/from-user-email/{user_email}/", response_model=list[OrderSchema])
async def get_orders_by_user_email_(user_email: str):
    return await get_orders_by_user_email(user_email) 


@app.get("/dishes/from-order/{order_id}/", response_model=list[DishSchema])
async def get_dishes_by_order_id_(order_id: int):
    return await get_dishes_by_order_id(order_id)


@app.get("/orders/from-dish/{dish_id}/", response_model=list[OrderSchema])
async def get_orders_by_dish_id_(dish_id: int):
    return await get_orders_by_dish_id(dish_id)



# @app.post("/orders/", response_model=OrderSchema)
# async def create_order_(dish_schema: DishCreateSchema):
#     new_order = await create_order(dish_schema)
#     return new_order
