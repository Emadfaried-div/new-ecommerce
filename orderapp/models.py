from django.db import models
from product .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField

# Create your models here.

class ShopCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField()


    def price(self):
        if self.product.discount_price:

           return self.product.discount_price
        else:
            return self.product.price
    @property
    def amount(self):
        if self.product.discount_price:
            
           return self.quantity*self.product.discount_price
        else:
            return self.quantity*self.product .price


    def __str__(self):
        return self.product.title

class ShopingCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']



class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
            )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=200)  
    last_name=models.CharField(max_length=200)       
    code=models.CharField(max_length=15,editable=False) 
    phone=models.CharField(max_length=200,blank=True, null=True)  
    address=models.CharField(max_length=200)   
    city=models.CharField(max_length=200)  
    country=models.CharField(max_length=200,null=True)
    total=models.FloatField()
    status = models.CharField(choices=STATUS, max_length=20, default='New')
    ip = models.CharField(max_length=200, blank=True)
    transaction_id = models.CharField(max_length=200, blank=True)
    transaction_image = models.ImageField(
        upload_to='transaction_image/', blank=True)
    adminnote = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.transaction_image.url))
    image_tag.short_description = 'Image'



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'phone', 'address', 'city', 'country', 'transaction_id', 'transaction_image']



class OrderProduct(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
    @property
    def amountnow(self):
        if self.product .discount_price:
            
           return self.quantity*self.product.discount_price
        else:
            return self.quantity*self.product.price                  




