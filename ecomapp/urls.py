
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
    path("all-products/",all_product_view,name="allproducts")   #to show by product name
    
]