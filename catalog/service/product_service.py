from catalog.models import *
import os
import random
from typing import List


def create(name: str, desc: str, category_names: List[str], images) -> object:
    product = Product.objects.create(product_name=name, description=desc)
    for category in category_names:
        category_object = Category.objects.get(name=category)
        product.category.add(category_object)
    for img in images:
        ProductImage.objects.create(img=img, product=product)
    return product


def retrieve() -> List[object]:
    product = Product.objects.all()
    return product


def retrieve_id(product_id: int) -> object:
    product = Product.objects.get(id=product_id)
    return product


def update(product_id: int, product_newname: str, product_desc: str, product_images) -> object:
    new_product = Product.objects.get(id=product_id)
    print(product_images)
    if len(product_images) > 0:
        images = new_product.product_image.all()
        for img in images:
            if len(img.img) > 0:
                os.remove(img.img.path)
        images.delete()
        for img in product_images:
            ProductImage.objects.create(img=img, product=new_product)
    new_product.product_name = product_newname
    new_product.description = product_desc
    new_product.save()
    return new_product


def delete(product_id: int) -> None:
    product = Product.objects.get(id=product_id)
    product_image = product.product_image.all()
    for img in product_image:
        if len(img.img) > 0:
            os.remove(img.img.path)
    product_image.delete()
    product.delete()
    return None


def randomize(product_model) -> List[object]:
    items = list(product_model.objects.all())
    # change 3 to how many random items you want
    random_items = random.sample(items, 15)
    # if you want only a single random item
    # random_item = random.choice(items)
    return random_items


def category_product() -> tuple[object, object]:
    category = Category.objects.exclude(parent__isnull=False)
    product = randomize(Product)
    return category, product
