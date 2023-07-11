from app.db import get_db
from app.models import User, Dish, OrderDish, Order, Category, CategoryEnum


with get_db() as db:
    user1 = User(name="user1", password="user123", email="example@yandex.ru")
    user2 = User(name="user2", password="user1223", email="example2@yandex.ru")

    for user in [user1, user2]:
        db.add(user)
        db.commit()
        db.refresh(user)

    breakfast = Category(name=CategoryEnum.BREAKFAST)
    lunch = Category(name=CategoryEnum.LUNCH)
    dinner = Category(name=CategoryEnum.DINNER)

    for category in [breakfast, lunch, dinner]:
        db.add(category)
        db.commit()
        db.refresh(category)

# dish1 самый читабельный

    dish1 = Dish(name='dish1', description='dishDesc', price=100, category=breakfast)
    dish2 = Dish(name='dish2', description='dishDesc2', price=200)
    dish2.category = breakfast
    dish3 = Dish(name='dish3', description='dishDesc3', price=300, category_id=dinner.id)

    for dish in [dish1, dish2, dish3]:
        db.add(dish)
        db.commit()
        db.refresh(dish)

    order1 = Order(user=user1)
    order1_dishes = [dish1, dish2, dish3]
    for dish in order1_dishes:
        order_dish = OrderDish(order=order1, dish=dish)
        db.add(order_dish)
    db.add(order1)


    order2 = Order(user=user2)
    order2_dishes = [
        (dish1, 2),
        (dish3, 12),
    ]
    for dish, quantity in order2_dishes:
        order_dish = OrderDish(order=order2, dish=dish, quantity=quantity)
        db.add(order_dish)
    db.add(order2)


