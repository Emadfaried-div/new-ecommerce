from django.urls import path
from .views import *

app_name="product"

urlpatterns = [
    path("comment_add/<int:id>/",Comment_Add,name="Comment_Add"),
    
]
 
