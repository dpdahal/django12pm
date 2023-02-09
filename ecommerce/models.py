from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name

    def total_products(self):
        if self.product_set.count():
            return self.product_set.count()
        else:
            return "No Products"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products')

    def __str__(self):
        return self.product.name


class Banner(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/banners')
    is_active = models.BooleanField(default=True)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name


class Setting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='media/icon')
    logo = models.ImageField(upload_to='media/logo')
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
