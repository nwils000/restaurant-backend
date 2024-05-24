from django.db import models

class FoodType(models.Model):
    name = models.CharField(max_length=100)

class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=200)

class FoodItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    cuisine_type = models.ForeignKey(FoodType, on_delete=models.PROTECT)
    category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)

class Order(models.Model):
    total_price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    order_status = models.CharField(default='Unfulfilled', max_length=100)
    customer_who_ordered = models.ManyToManyField(Customer, through='CustomerOrderLink')

class CustomerOrderLink(models.Model):
    total_price = models.DecimalField(decimal_places=2, max_digits=5)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customer_orders')
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food_order_details = models.ManyToManyField(FoodItem, through='FoodOrderDetail')

class FoodOrderDetail(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    customer_order_detail = models.ForeignKey(CustomerOrderLink, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    special_requests = models.TextField()

    

    