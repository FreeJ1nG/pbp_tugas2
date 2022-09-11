from django.urls import path
from shop.views import (index, add_to_cart, reduce_from_cart)

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('add_to_cart/<str:item_uuid>/', add_to_cart, name="add_to_cart"),
    path('reduce_from_cart/<str:item_uuid>/', reduce_from_cart, name="reduce_from_cart"),
]