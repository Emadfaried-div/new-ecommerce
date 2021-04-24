from django.urls import path
from .views import Add_to_Shoping_cart,cart_details, cart_delete
app_name="orderapp"
urlpatterns=[
    path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path("cart_details/" ,cart_details, name="cart_details"),
    path('cart_delete/<int:id>/', cart_delete, name='cart_delete'),
]