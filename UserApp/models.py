from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from django.core.mail import send_mail
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    address=models.CharField(max_length=200,blank=True, null=True)
    address_ar =models.CharField(max_length=200,blank=True, null=True)
    city=models.CharField(max_length=100,blank=True, null=True)
    city_ar=models.CharField(max_length=100,blank=True, null=True)
    country=models.CharField(max_length=200,null=True)
    country_ar=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='user_image',blank=True, null=True)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + '' +self.user.last_name +'['+self.user.username+']'

    def  image_tag(self):
    	 return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))
    image_tag.short_description='Image'

    def imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return""

    


