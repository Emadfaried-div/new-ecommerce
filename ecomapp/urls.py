
from django.urls import path

from .views import home,SingleProductView, category_product, about

app_name= "ecomapp"

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"),
    path("product/<slug:slug>/",SingleProductView.as_view(), name="product_single"),
    path("product/<int:id>/<slug:slug>/",category_product, name="category_product"),
]