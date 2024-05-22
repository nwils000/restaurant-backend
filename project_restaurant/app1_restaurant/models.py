from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField()
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class Order(models.Model):
    total_price = models.DecimalField()
    order_status = models.CharField(max_length=100)

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

class CustomerOrderLink(models.Model):
    total_price = models.DecimalField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

class CustomerOrderDetail(models.Model):
    customer_order_link = models.ForeignKey(CustomerOrderLink, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    order_time = models.DateTimeField
    notes = models.TextField()

class OrderDetail(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    customer_order_detail = models.ForeignKey(CustomerOrderDetail, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    special_requests = models.TextField()
