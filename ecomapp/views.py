from django.shortcuts import render
from ecomapp.models import Setting
from product.models import Product


# Create your views here.
def home(request):
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by("id")[:2]
    context={"setting":setting,
            "sliding_images":sliding_images
    
            }
   
    return render(request, "home.html", context)



    