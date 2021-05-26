from django.db import models
from django import forms
from django.contrib.auth.models import User
from product.models import Product
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
# Create your models here.

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title=_("title")
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100, blank=True, null=True)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ContactMessage(models.Model):
    STATUS=(
        ("New","New"),
        ("Read","Read"),
        ("Closed","Closed"),
        )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS, default="New")
    ip= models.CharField(max_length=100,blank=True, null=True)
    note = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(choices=STATUS, max_length=200, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question



class BroadCast_Email(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    message = RichTextField(blank=False, null=False)

    
    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "BroadCast Email to all Member"
        verbose_name_plural = "BroadCast Email"
         
        
class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="banner/")

    def __str__(self):
        return self.title