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



class DishSchema(BaseModel):
    id: int
    name: str
    description: str
    image: str
    price: int
    category: CategorySchema

    class Config:
        orm_mode = True


class OrderSchema(BaseModel):
    id: int
    user: UserSchema
    created_at: str

    class Config:
        orm_mode = True
