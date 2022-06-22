from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category_image = models.ImageField(upload_to='images/category', null=True)

    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # brand = models.ForeignKey(Brand, related_name='b_products', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='c_products')

    def __str__(self):
        return self.product_name


class ProductComments(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name


class ProductViews(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    img = models.ImageField(upload_to='images/product', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.img
