from django.db import models

# Create your models here.

class Category(models.Model):
    status=(
        ("True","True"),
        ("False","False"),
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="category/")
    status = models.CharField(max_length=50,choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.title

    parent = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, related_name="children")


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
    amoun = models.FloatField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = models.TextField()
    status= models.CharField(max_length=50,choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title