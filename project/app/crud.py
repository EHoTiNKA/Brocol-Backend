from app.models import User, Dish, OrderDish, Order, Category
from app.schemas import UserSchema, DishSchema, OrderSchema, CategorySchema, DishCreateSchema, DishUpdateSchema
from tortoise import functions


async def get_user_by_email(email: str) -> User or None:
    return await User.get_or_none(email=email)

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


async def create_dish(dish_schema: DishCreateSchema) -> Dish:
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


async def update_dish(dish_schema: DishUpdateSchema) -> Dish:
    dish = await get_dish_by_id(dish_schema.id)
    update_dict = dish_schema.dict(exclude_unset=True)
    if "category_id" in update_dict:
        update_dict["category"] = await get_category_by_id(update_dict.pop("category_id"))

    await dish.update_from_dict(update_dict)
    await dish.save()
    return dish
 

async def get_order_list() -> list[Order]:
    return await Order.annotate(
        unique_dishes_count=functions.Count("order_dish"),
        dishes_count=functions.Sum("order_dish__quantity")
    ).all().prefetch_related('user')


async def get_order_by_id(order_id: int) -> Order or None:
    return await Order.get_or_none(id=order_id).prefetch_related('user')

async def get_orders_by_user_id(user_id: int) -> list[Order]:
    return await Order.filter(user_id=user_id).prefetch_related('user')

async def get_orders_by_user_email(user_email: str) -> list[Order]:
    return await Order.filter(user__email=user_email).prefetch_related('user')


async def get_dishes_by_order_id(order_id: int) -> list[Dish]:
    return await Dish.filter(order_dish__order_id=order_id).prefetch_related('category')

async def get_orders_by_dish_id(dish_id: int) -> list[Order]:
    return await Order.filter(order_dish__dish_id=dish_id).prefetch_related('user')