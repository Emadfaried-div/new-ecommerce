from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from ecomapp.models import *
from product.models import *
from django.contrib import messages
from .forms import *
from django.views.generic import  TemplateView
from django.urls import reverse
import product
from orderapp.models import *
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.core.paginator import Paginator
from idlelib import query


# Create your views here.
def home(request):
        #from django.utils import translation
       # user_language= 'ar'
        #tranlation.activate=(user_language)
        #if translation.LANGUAGE_SESSION_KEY in request.session:    
               # del request.session[translation.LANGUAGE_SESSION_KEY]  
        
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
        sliding_images = Product.objects.all().order_by('-id')  [:9]
        latest_products = Product.objects.all().order_by("-id")
        
        products = Product.objects.all().order_by("id")
        fashionproducts=Product.objects.all().order_by("id")
        
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
                "products":products,
               
                
                }
                if single_product.variant != "None":  # Product have variants

                        if self.request.method == 'POST':  # if we select color
                                variant_id = self.request.POST.get('variantid')
                                variant = Variants.objects.get(id=variant_id)  # selected product by click color radio
                                colors = Variants.objects.filter(product_id=id, size_id=variant.size_id)
                                sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
                                query += variant.title+' Size:' + str(variant.size) + ' Color:' + str(variant.color)
                        else:
                                variants = Variants.objects.filter(product_id=id)
                                colors = Variants.objects.filter(product_id=id, size_id=variants[0].size_id)
                                sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
                                variant = Variants.objects.get(id=variants[0].id)
                                context.update({'sizes': sizes, 'colors': colors,
                                        'variant': variant, 'query': query
                                        })
                return context


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)






def category_product(request,id, slug):
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        sliding_images = Product.objects.all().order_by('id')  [:3]
        product_cat=Product.objects.filter(category_id=id)
        products = Product.objects.all().order_by("id")[:5]
        page_number = request.GET.get('page')
        paginator = Paginator(products, 3)
        product_list = paginator.get_page(page_number)
        paginate_by= 3
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



def send(request):
        send_mail("Hello","Hello there. this is automated message!","nemhfa@gmail.com",["efaried@icloud.com"],fail_silently=False)
        return (request,"send_email.hmtl")




class OffersView(TemplateView): #for Tv,laptops
    paginate_by= 8
    model=Product
    
    template_name = "offers.html"
    
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products=Product.objects.all().order_by("name")
        page_number = self.request.GET.get('page')
        paginator = Paginator(products, 8)
        product_list = paginator.get_page(page_number)
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        faq = FAQ.objects.filter(status=True).order_by('created_at')
        
        
        context={
                'products':products,
                'category': category,
                'setting': setting,
                'faq': faq,
                'product_list':product_list,
        }
        return context



class OffersView2(TemplateView): #mobiles
    paginate_by= 4
    model=Product
    
    template_name = "offers2.html"
    
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products=Product.objects.all()
        page_number = self.request.GET.get('page')
        paginator = Paginator(products, 4)
        product_list = paginator.get_page(page_number)
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        faq = FAQ.objects.filter(status=True).order_by('created_at')
        
        
        context={
                'products':products,
                'category': category,
                'setting': setting,
                'faq': faq,
                'product_list':product_list,
        }
        return context




class OffersView3(TemplateView): #mobiles
    paginate_by= 4
    model=Product
    
    template_name = "offers3.html"
    
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products=Product.objects.all()
        page_number = self.request.GET.get('page')
        paginator = Paginator(products, 4)
        product_list = paginator.get_page(page_number)
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        faq = FAQ.objects.filter(status=True).order_by('created_at')
        
        
        context={
                'products':products,
                'category': category,
                'setting': setting,
                'faq': faq,
                'product_list':product_list,
        }
        return context        


       
def all_product_view(request):   #for All LAPTOP PRODUCTS
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products.html', context)


def all_product_view2(request):    #FOR ALL TV PRODUCTS          
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products2.html', context)


def all_product_view3(request):    #FOR ALL HOME APPLIANCES         
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=4
        paginator = Paginator(all_products, 4)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products3.html', context)        


def all_product_view4(request):    #FOR ALL MOBILES          
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products4.html', context)


def all_product_view5(request):    #FOR ALL BESTSELLER         
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products5.html', context)        

def all_product_view6(request):    #FOR ALL TABLETS         
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products6.html', context)        



def all_product_view7(request):    #FOR ALL FASHIONS          
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 2)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products7.html', context)        



def all_product_view8(request):    #FOR ALL TOOLS           
        all_products=Product.objects.all()
        category= Category.objects.all()
        setting= Setting.objects.get(id=1)
        paginate_by=2
        paginator = Paginator(all_products, 16)
        page_number = request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context={
                'all_products':all_products,
                'category': category,
                'setting': setting,
                "product_list":product_list,
        }

        return render(request, 'all_products8.html', context)        




