from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from ecomapp.models import *
from product.models import *
from django.contrib import messages
from .forms import *
from django.views.generic import  TemplateView
from django.urls import reverse
import product
from orderapp.models import *

    



# Create your views here.
def home(request):
        current_user = request.user
        cart_product= ShopCart.objects.filter(user_id=current_user.id)
        total_amount = 0
        for p in cart_product:
            if p.product.discount_price:
                total_amount += p.product.discount_price * p.quantity
            elif p.product.price:
                    
                total_amount += p.product.price * p.quantity
                        
                





        category= Category.objects.all()
        setting = Setting.objects.get(id=1)
        sliding_images = Product.objects.all().order_by('id')  [:4]
        latest_products = Product.objects.all().order_by("-id")
        products = Product.objects.all()
        
        context={"setting":setting,
                "sliding_images":sliding_images,
            "latest_products":latest_products,
            "products":products,
            "category":category,
            "cart_product":cart_product,
                "total_amount":total_amount,
    
            }
   
        return render(request, "home.html", context)


def about(request):
        setting = Setting.objects.get(id=1)
        category= Category.objects.all()
        context={"setting":setting,
        "category":category,}
        return render(request,"about.html", context)


def contact(request):

        if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                        data = ContactMessage()
                        data.name = form.cleaned_data['name']
                        data.email = form.cleaned_data['email']
                        data.subject = form.cleaned_data['subject']
                        data.message = form.cleaned_data['message']
                        data.ip = request.META.get('REMOTE_ADDR')
                        data.save()
                        #messages.success(request, 'Profile details updated.')
                        return redirect('contact_dat')
        setting = Setting.objects.get(pk=1)
        category= Category.objects.all()
        form = ContactForm
        context = {
                        'setting': setting,
                        'form': form,
                        "category":category,
                }
        messages.success(request, 'Your message was successfully sent.')
        return render (request, "contact_form.html", context )
                


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
#                comment_show = Comment.objects.filter(product_id=id, status='True')
                category= Category.objects.all()
               
                single_product.save()
                single_product.min_amount==1
                context={"setting":setting,
                "single_product":single_product,
                "images":images,
                "category":category,
                #"comment_show":comment_show,
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



def searchview(request):
        if request.method=="GET":
                form=SearchForm(request.GET)  
                if form.is_valid():
                        query = form.cleaned_data['query']
                        cat_id = form.cleaned_data['cat_id']
                        if cat_id == 0:
                                products = Product.objects.filter(title__icontains=query)
                        else:
                                products = Product.objects.filter(
                                        title__icontains=query, category_id=cat_id
                                )
                        category = Category.objects.all()
                        setting= Setting.objects.get(id=1)
                        sliding_images = Product.objects.all().order_by('id')  [:4]
                        context = {
                                "category":category,
                                "query":query,
                                "product_cat":products,
                                "setting":setting,
                                "sliding_images":sliding_images,
                        }
                        return render (request, "category_product.html", context)
        return HttpResponseRedirect("category_product")

def Faq_details(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    faq = FAQ.objects.filter(status=True).order_by('created_at')

    context = {
        'category': category,
        'setting': setting,
        'faq': faq

    }
    return render(request, 'faq.html', context)