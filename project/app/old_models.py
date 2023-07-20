import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import backref, declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    orders = relationship("Order", backref=backref("user"))

    def __str__(self):
        return f"User(id={self.id}, name={self.email})"


class CategoryEnum(PyEnum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Enum(CategoryEnum), nullable=False)

    dishes = relationship("Dish", backref=backref("category"))


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    order_dishes = relationship("OrderDish", backref=backref("order"))

    def __str__(self):
        return f"Order(id={self.id}, user={self.user.name}, created_at={self.created_at})"


class OrderDish(Base):
    __tablename__ = "ordersdish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    dish_id = Column(Integer, ForeignKey("dish.id"), nullable=False)
    quantity = Column(Integer, default=1)


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    image = Column(String(255))
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    order_dishes = relationship("OrderDish", backref=backref("dish"))

    def __str__(self):
        return f"Dish(id={self.id}, name={self.name}, price={self.price}, category={self.category.name.value})"
