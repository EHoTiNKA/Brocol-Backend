from app.db import get_db
from app.models import User, Dish, OrderDish, Order, Category
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema


def get_category_by_id(category_id: int) -> CategorySchema or None:
    with get_db() as db:
        category = db.query(Category).filter(Category.id == category_id).first()
        if not category:
            return None
        return CategorySchema(
            id=category.id,
            name=category.name
        )


def get_category_list() -> list[CategorySchema]:
    with get_db() as db:
        category_list = db.query(Category).all()
        return [
            CategorySchema(
            id=category.id,
            name=category.name
            ) for category in category_list
        ]
    