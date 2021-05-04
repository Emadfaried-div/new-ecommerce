from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.forms import ModelForm
from django.db.models import Count,Sum,Avg

# Create your models here.

class Category(MPTTModel):
    status=(
        ("True","True"),
        ("False","False"),
    )
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="category/")
    status = models.CharField(max_length=50,choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)


    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    


class Product(models.Model):
    status=(
        ("True","True"),
        ("False","False"),
    )
    title= models.CharField(max_length=200)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    keywords = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="product/")
    discount_price= models.PositiveIntegerField(default=0,blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    amount = models.FloatField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status= models.CharField(max_length=50,choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{} " heights="70" width="60" \> '.format(self.image.url))
    image_tag.short_description="image" 

    def average_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(average=Avg('rate'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
        else:
            return avg

    def total_review(self):
        reviews = Comment.objects.filter(
            product=self, status=True).aggregate(count=Count('id'))
        cnt = 0
        if reviews['count'] is not None:
            cnt = (reviews['count'])
            return cnt



    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""   

    def get_absolute_url(self):

        return reversed("product_element", kwargs={'slug':self.slug})       

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=20,blank=True)
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title



class Comment(models.Model):
    STATUS=(
        ("New","New"),
        ("True","True"),
        ("False","False"),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=200,blank=True, null=True)
    comment=models.CharField(max_length=500,blank=True)
    rate=models.PositiveIntegerField(default=1)
    ip=models.CharField(max_length=100,blank=True)
    status=status= models.CharField(max_length=50,choices=STATUS,default="new")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommenttForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["subject","comment","rate"]
   

    