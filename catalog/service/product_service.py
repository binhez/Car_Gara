from catalog.models import *
import os
import random
from django.core.paginator import Paginator

def create(name, desc, category, images):
    product = Product.objects.create(product_name=name, description=desc)
    for c in category:
        category_object = Category.objects.get(name=c)
        product.category.add(category_object)
    for img in images:
        ProductImage.objects.create(img=img, product=product)
    return True
def retrieve():
    product = Product.objects.all()
    return product
def retrieve_id(id):
    product = Product.objects.get(id=id)
    return product
def update(id, newname, newdesc, newimgs):
    new_product = Product.objects.get(id=id)
    print(newimgs)
    if len(newimgs) > 0:
        imgs = new_product.product_image.all()
        for img in imgs:
            if len(img.img) > 0:
                os.remove(img.img.path)
        imgs.delete()
        for img in newimgs:
            ProductImage.objects.create(img=img, product=new_product)
    new_product.product_name = newname
    new_product.description = newdesc
    new_product.save()
    return True
def delete(id):
    product = Product.objects.get(id=id)
    product_image = product.product_image.all()
    for img in product_image:
        if len(img.img) > 0:
            os.remove(img.img.path)
    product_image.delete()
    product.delete()
    return True
def randomize(Product):
    items = list(Product.objects.all())
    # change 3 to how many random items you want
    random_items = random.sample(items, 10)
    # if you want only a single random item
    # random_item = random.choice(items)
    return random_items
def category_product():
    category = Category.objects.exclude(parent__isnull=False)
    product = randomize(Product)
    return category, product