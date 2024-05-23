from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    
class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerOrderLinkViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrderLink.objects.all()
    serializer_class = CustomerOrderLinkSerializer

class CustomerOrderDetailViewSet(viewsets.ModelViewSet):
    queryset = CustomerOrderDetail.objects.all()
    serializer_class = CustomerOrderDetailSerializer

class FoodOrderDetailViewSet(viewsets.ModelViewSet):
    queryset = FoodOrderDetail.objects.all()
    serializer_class = FoodOrderDetailSerializer

class AllFoodInformationViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = AllFoodInformationSerializer
