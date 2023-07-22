from app.models import User, Dish, OrderDish, Order, Category
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema, CreateDishSchema


async def get_category_by_id(category_id: int) -> Category or None:
    return await Category.get_or_none(id=category_id)


async def get_category_list() -> list[CategorySchema]:
    return await Category.all()

async def create_category(name: str) -> Category:
    category = await Category.create(name=name)
    return category

async def get_dish_list(category_id: int | None = None) -> list[Dish]:
    if category_id is None:
        return await Dish.all().prefetch_related('category')
    return await Dish.filter(category_id=category_id).prefetch_related("category")

async def create_dish(dish_schema: CreateDishSchema) -> Dish:
    dish = await Dish.create(
        name=dish_schema.name,
        description=dish_schema.description,
        image=dish_schema.image,
        price=dish_schema.price,
        category= await get_category_by_id(dish_schema.category_id)
    )
    return dish
