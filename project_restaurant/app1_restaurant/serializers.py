from rest_framework import serializers
from .models import *

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'name']     

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', 'name']

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'title', 'description', 'price', 'cuisine_type', 'category']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'order_status', 'customer_who_ordered']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'contact_information']

class CustomerOrderLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrderLink
        fields = ['id', 'total_price', 'customer', 'order']

class CustomerOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrderDetail 
        fields = ['id', 'customer_order_link', 'order_time', 'notes']

class FoodOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrderDetail
        fields = ['id', 'food_item', 'customer_order_detail', 'quantity', 'special_requests']

class AllFoodInformationSerializer(serializers.ModelSerializer):
    cuisine_type = FoodTypeSerializer(read_only=True)
    category = FoodCategorySerializer(read_only=True)
    class Meta:
        model = FoodItem
        fields = ['id', 'title', 'description', 'price', 'cuisine_type', 'category']