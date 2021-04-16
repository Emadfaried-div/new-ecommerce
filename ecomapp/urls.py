
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
]