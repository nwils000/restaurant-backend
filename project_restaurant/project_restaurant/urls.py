"""
URL configuration for project_restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers

from app1_restaurant.views import *

router = routers.DefaultRouter()

router.register(r'food-type', FoodTypeViewSet)
router.register(r'food-category', FoodCategoryViewSet)
router.register(r'food-items', FoodItemViewSet)
router.register(r'order', OrderViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customer-order-link', CustomerOrderLinkViewSet)
router.register(r'customer-order-detail', CustomerOrderDetailViewSet)
router.register(r'food-order-detail', FoodOrderDetailViewSet)
router.register(r'all-food-information', AllFoodInformationViewSet, basename='allfoodinfo')

urlpatterns = [
    path('', include(router.urls))
]