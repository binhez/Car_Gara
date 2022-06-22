from catalog.models import *
import os
from django.core.paginator import Paginator


def create(name: str, desc: str, img) -> object:
    category = Category.objects.update_or_create(name=name, description=desc, category_image=img)
    return category


def retrieve() -> list[object]:
    list_category = Category.objects.all()
    return list_category


def retrieve_id(category_id: int) -> object:
    category = Category.objects.get(id=category_id)
    return category


def update(category_id: int, category_name: str, category_desc: str, category_img) -> object:
    new_category = Category.objects.get(id=category_id)
    img = new_category.category_image
    if len(img) > 0:
        os.remove(img.path)
    new_category.name = category_name
    new_category.description = category_desc
    new_category.category_image = category_img
    new_category.save()
    return new_category


def delete(category_id: int) -> None:
    category = Category.objects.get(id=category_id)
    img = category.category_image
    if len(img) > 0:
        os.remove(img.path)
    img.delete()
    category.delete()
    return None


def paginator(request, obj: object) -> list[object]:
    paginator_object = Paginator(obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator_object.get_page(page_number)
    return page_obj


def draw_tree() -> dict:
    tree_category = {}
    list_category = retrieve()
    for category in list_category:
        tree_category[category.id] = category.children.all()

    return tree_category


def make_tree(parent_id, children_id) -> None:
    parent = Category.objects.get(id=parent_id)
    child = Category.objects.get(id=children_id)
    child.parent = parent
    child.save()
    return None
