from django.shortcuts import render, HttpResponse
from ecomapp.models import Setting
from product.models import Product, Images, Category
from django.views.generic import  TemplateView
    



# Create your views here.
def home(request):
        category= Category.objects.all()
        setting = Setting.objects.get(id=1)
        sliding_images = Product.objects.all().order_by('id')  [:2]
        latest_products = Product.objects.all().order_by("-id")
        products = Product.objects.all()
        
        context={"setting":setting,
                "sliding_images":sliding_images,
            "latest_products":latest_products,
            "products":products,
            "category":category,
    
            }
   
        return render(request, "home.html", context)


def about(request):
        setting = Setting.objects.get(id=1)
        category= Category.objects.all()
        context={"setting":setting,
        "category":category,}
        return render(request,"about.html", context)


class SingleProductView(TemplateView):
        model = Product
        template_name = "product-single.html"
        def get_context_data(self, **kwargs):
                context= super().get_context_data(**kwargs)
                url_slug = self.kwargs["slug"]
                single_product = Product.objects.get(slug=url_slug)
                setting= Setting.objects.get(id=1)
                images = Images.objects.filter(product__slug=url_slug)
                products = Product.objects.all().order_by("id")[:5]
                category= Category.objects.all()
                single_product.save()
                context={"setting":setting,
                "single_product":single_product,
                "images":images,
                "category":category,
                "products":products}
                return context

def category_product(request,id, slug):
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        sliding_images = Product.objects.all().order_by('id')  [:4]
        product_cat=Product.objects.filter(category_id=id)

        context={"product_cat":product_cat,
                "sliding_images":sliding_images,
                "setting":setting,
                "category":category,
        }
                      
        return render(request,"category_product.html",context)



    