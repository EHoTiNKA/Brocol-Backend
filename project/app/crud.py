from app.models import User, Dish, OrderDish, Order, Category
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema, CreateDishSchema, UpdateDishSchema


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


async def get_dish_by_id(dish_id: int) -> Dish or None:
    return await Dish.get_or_none(id=dish_id).prefetch_related("category")


async def update_dish(dish_schema: UpdateDishSchema) -> Dish:
    dish = await get_dish_by_id(dish_schema.id)
    update_dict = dish_schema.dict(exclude_unset=True)
    if "category_id" in update_dict:
        update_dict["category"] = await get_category_by_id(update_dict.pop("category_id"))

    await dish.update_from_dict(update_dict)
    await dish.save()
    return dish
 

async def get_order_list() -> list[OrderSchema]:
    return await Order.all


async def get_order_by_id(order_id: int) -> Order or None:
    return await Order.get_or_none(id=order_id)
