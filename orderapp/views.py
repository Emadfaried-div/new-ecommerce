from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from django.views.generic import ListView, TemplateView , DetailView , View, CreateView, FormView
from product.models import Category, Product, Images
from django.contrib import messages
from orderapp .models import *
from ecomapp.models import Setting, ContactMessage
from ecomapp.models import *
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from UserApp.models import UserProfile

# Create your views here.


@login_required()
def Add_to_Shoping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(
        product_id=id, user_id=current_user.id)
        
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(
                    product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Your Product  has been added')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.filter(
            product_id = id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            
            data.quantity = 1
            data.save()
        messages.success(request, 'Your  product has been added')
        return HttpResponseRedirect(url)


def cart_details(request):
    
    current_user = request.user
    category= Category.objects.all()
    setting = Setting.objects.get(id=1)
    cart_product= ShopCart.objects.filter(user_id=current_user.id)
    
    total_amount = 0
    
    for p in cart_product:
        
        if p.product.discount_price:
            total_amount += p.product.discount_price * p.quantity
        elif p.product.price:
            total_amount += p.product.price * p.quantity

    context = {"category":category,
                "setting":setting,
                "cart_product":cart_product,
                "total_amount":total_amount,
                
            }
    return render(request,"cart_details.html", context)


@login_required()
def cart_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart_product= ShopCart.objects.filter(id=id,user_id=current_user.id)
    cart_product.delete()
    messages.warning(request, 'Your  product has been deleted successfully!!')
    return HttpResponseRedirect(url)




@login_required()
def OrderCart(request):
    current_user=request.user
    
    shoping_cart=ShopCart.objects.filter(user_id=current_user.id)
    totalamount=0
    for rs in shoping_cart:
        if rs.product.discount_price:
            totalamount += rs.product.discount_price * rs.quantity
        elif rs.product.price:
            totalamount += rs.product.price * rs.quantity
    if request.method=="POST":
        form=OrderForm(request.POST,request.FILES)
        if form.is_valid():
            dat =Order()
            dat.first_name=form.cleaned_data["first_name"]
            dat.last_name = form.cleaned_data['last_name']
            dat.address = form.cleaned_data['address']
            dat.city = form.cleaned_data['city']
            dat.phone = form.cleaned_data['phone']
            dat.country = form.cleaned_data['country']
            dat.transaction_id = form.cleaned_data['transaction_id']
            dat.transaction_image = form.cleaned_data['transaction_image']
            dat.user_id = current_user.id
            
            dat.total = totalamount
            dat.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(length=12, allowed_chars='ABCDE01234')  # random cod
            dat.code = ordercode
            dat.save()
            for rs in shoping_cart:
                data = OrderProduct()
                data.order_id = dat.id
                data.product_id = rs.product_id
                
                data.user_id = current_user.id
                data.quantity = rs.quantity
                if rs.product.discount_price:
                    data.price = rs.product.discount_price
                else:
                    data.price = rs.product.price 
                
                data.amount = rs.amount
                data.save()

                product = Product.objects.get(id=rs.product_id)
                
                
                product.amount -= rs.quantity
                
                product.save()
                
            # Now remove all oder data from the shoping cart
            ShopCart.objects.filter(user_id=current_user.id).delete()
            # request.session['cart_item']=0
            messages.success(request, 'Your order has been completed')
            category = Category.objects.all()
            setting = Setting.objects.get(id=1)
            context = {
                # 'category':category,
                'ordercode': ordercode,
                'category': category,
                'setting': setting,
            }

            return render(request, 'order_completed.html', context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/order_cart")
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    total_amount = 0
    for p in shoping_cart:
        if p.product.discount_price:
            total_amount += p.product.discount_price * p.quantity
        else:
            total_amount += p.product.price * p.quantity
        
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)

    context = {
        # 'category':category,
        'shoping_cart': shoping_cart,
        'totalamount': totalamount,
        'profile': profile,
        'form': form,
        'category': category,
        'setting': setting,
        'total_amount': total_amount
    }
    return render(request, 'order_form.html', context)

@login_required()
def Order_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'orders': orders

    }

    return render(request, 'user_order_showing.html', context)

@login_required()
def Order_Product_showing(request):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'order_product': order_product

    }

    return render(request, 'OrderProducList.html', context)



@login_required()
def user_order_details(request,id):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    orders = Order.objects.get(user_id=current_user.id,id=id)
    order_products = OrderProduct.objects.filter(order_id=id)
    context = {
        'category': category,
        'setting': setting,
        'orders': orders,
        'order_products':order_products,

    }

    return render(request,'user_order_details.html', context)


@login_required()
def userorderproduct_details(request,id,oid):
    category = Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    orders = Order.objects.get(user_id=current_user.id,id=oid)
    order_products = OrderProduct.objects.get(user_id=current_user.id,id=id)
    context = {
        'category': category,
        'setting': setting,
        'orders': orders,
        'order_products':order_products,

    }

    return render(request,'user_order_pro_details.html', context)    
    



