from enum import Enum as PyEnum

from tortoise.models import Model
from tortoise import fields


class User(Model):
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)


class CategoryEnum(PyEnum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"


class Category(Model):
    name = fields.CharField(max_length=255)
        

class Order(Model):
    user = fields.ForeignKeyField('models.User', related_name='orders')
    created_at = fields.DatetimeField(auto_now_add=True)


class Dish(Model):
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.FloatField()
    image = fields.CharField(max_length=255)
    category = fields.ForeignKeyField('models.Category',  related_name='dishes')


class OrderDish(Model):
    quantity = fields.IntField()
    order = fields.ForeignKeyField('models.Order',  related_name='order_dish')
    dish = fields.ForeignKeyField('models.Dish',  related_name='order_dish')





   


