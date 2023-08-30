from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class CategoryCreateSchema(BaseModel):
    name: str


class CategorySchema(CategoryCreateSchema):
    id: int

    class Config:
        orm_mode = True


class DishBaseSchema(BaseModel):
    name: str
    description: str
    image: str | None = None
    price: int


class DishCreateSchema(DishBaseSchema):
    category_id: int


class DishSchema(DishBaseSchema):
    id: int
    category: CategorySchema

    class Config:
        orm_mode = True


class DishUpdateSchema(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None
    image: str | None = None
    price: int | None = None
    category_id: int | None = None


class OrderSchema(BaseModel):
    id: int
    user: UserSchema
    created_at: datetime

    class Config:
        orm_mode = True


class OrderWithDishSchema(OrderSchema):
    unique_dishes_count: int
    dishes_count: int

    class Config:
        orm_mode = True

class OrderCreateSchema(BaseModel):
    user_id: int
    dish_id_list: list[int]
    dish_quantity_list: list[int] 
    