from app.db import get_db
from app.models import User, Dish, OrderDish, Order, Category


with get_db() as db:
    users = db.query(User).all()
    print(users)

    for user in users:
        print(user)

    print()

    dishes = db.query(Dish).all()
    for dish in dishes:
        print(dish)
        order_dishes = dish.order_dishes
        for order_dish in order_dishes:
            print(f"\t{dish.name}\tin = {order_dish.order}")

    print()

    orders = db.query(Order).all()
    for order in orders:
        print(order)
        # dishes = db.query(Dish).join(OrderDish).filter(OrderDish.order_id == order.id).all()
        order_dishes = order.order_dishes
        for order_dish in order_dishes:
            print(f"\tx = {order_dish.quantity}\t {order_dish.dish.name}")

    print()



    
