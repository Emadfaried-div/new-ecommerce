from django.urls import path

from orderapp.views import (Add_to_Shoping_cart,
OrderCart,Order_showing, Order_Product_showing,
cart_details, cart_delete, user_order_details, userorderproduct_details)

app_name="orderapp"

urlpatterns=[
    path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
    path("cart_details/" ,cart_details, name="cart_details"),
    path('cart_delete/<int:id>/', cart_delete, name='cart_delete'),
    path("order_cart/",OrderCart,name="OrderCart"),
    path("orderlist",Order_showing,name="orderlist"),
    path('OrderProduct/', Order_Product_showing, name="orderproduct"),
    path('OrderDetails/<int:id>/',user_order_details,name='user_order_details'),
    path('OrderproductDetails/<int:id>/<int:oid>/',userorderproduct_details,name='userorderproduct_details'),
    
    
]