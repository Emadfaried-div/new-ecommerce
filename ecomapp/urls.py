
from django.urls import path

from .views import *

app_name= "ecomapp"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contact/",contact, name="coantact_dat"),
    path("product/<slug:slug>/", SingleProductView.as_view(), name="product_single"),
    path("product/<int:id>/<slug:slug>/", category_product, name="category_product"),
    path("search/",searchview,name="searchview"),
    path("faq/",Faq_details,name="Faq_details"),
    path("send/",send,name="send"),
    path("offers/", OffersView.as_view(), name= "offers"), #for laptops and TV
    path("offers2/", OffersView2.as_view(), name= "offers2"), #OffersView2
    path("offers3/",OffersView3.as_view(), name="offers3"), # for home appliances  
    path("all-products/",all_product_view,name="allproducts"),   #to show All Laptops
    path("all-products2/",all_product_view2,name="allproducts2"),   #to show All TVs
    path("all-products3/",all_product_view3,name="allproducts3"),   #to show All home appliances 
    path("all-products4/",all_product_view4,name="allproducts4"),   #to show All mobiles
    path("all-products5/",all_product_view5,name="allproducts5"),   #to show All  tablets
    path("all-products6/",all_product_view6,name="allproducts6"),   #to show All bestseller
    path("all-products7/",all_product_view7,name="allproducts7"),   #to show All fashion
    path("all-products8/",all_product_view8,name="allproducts8"),   #to show All tools
    
    
]