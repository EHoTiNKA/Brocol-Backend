from pydantic import BaseModel

from app.models import CategoryEnum


class BaseModelORM(BaseModel):
    class Config:
        orm_mode = True


class UserSchema(BaseModelORM):
    id: int
    name: str
    email: str
    password: str

class CategorySchema(BaseModelORM):
    id: int
    name: CategoryEnum

class DishSchema(BaseModelORM):
    id: int
    name: str
    description: str
    image: str
    price: int
    category: CategorySchema

class OrderSchema(BaseModelORM):
    id: int
    user: UserSchema
    created_at: str

