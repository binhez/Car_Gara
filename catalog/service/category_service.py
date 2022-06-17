from catalog.models import *
import os
from django.core.paginator import Paginator

def create(name, desc, img):
    Category.objects.update_or_create(name=name, description=desc, category_image=img)
    return True
def retrieve():
    category = Category.objects.all()
    return category
def retrieve_id(id):
    category = Category.objects.get(id=id)
    return category
def update(id, newname, newdesc, newimg):
    new_category = Category.objects.get(id=id)
    img = new_category.category_image
    if len(img) > 0:
        os.remove(img.path)
    new_category.name = newname
    new_category.description = newdesc
    new_category.category_image = newimg
    new_category.save()
    return True
def delete(id):
    category = Category.objects.get(id=id)
    img = category.category_image
    if len(img) > 0:
        os.remove(img.path)
    img.delete()
    category.delete()
    return True
def paginator(request, object):
    paginator = Paginator(object, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
def maketree(p, c):
    parent = Category.objects.get(id=p)
    child = Category.objects.get(id=c)
    child.parent = parent
    child.save()
    return True
