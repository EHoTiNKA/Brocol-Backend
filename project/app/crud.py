from app.models import User, Dish, OrderDish, Order, Category
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema


async def get_category_by_id(category_id: int) -> Category or None:
    return await Category.get_or_none(id=category_id)


async def get_category_list() -> list[CategorySchema]:
    return await Category.all()
