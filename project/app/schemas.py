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


class CreateDishSchema(DishBaseSchema):
    category_id: int


class DishSchema(DishBaseSchema):
    id: int
    category: CategorySchema

    class Config:
        orm_mode = True


class OrderSchema(BaseModel):
    id: int
    user: UserSchema
    created_at: str

    class Config:
        orm_mode = True
