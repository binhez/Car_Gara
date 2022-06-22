from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import *
from catalog.service import category_service, product_service
from catalog.api.serializiers import CategorySerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
@login_required(login_url='user_app:login')
def home(request):
    category, product = product_service.category_product()
    return render(request, 'catalog/index.html', {'category': category, 'product': product})


def brand(request):
    return render(request, 'catalog/brand.html')


def contact(request):
    return render(request, 'catalog/contact.html')


class CreateCategory(View):
    @staticmethod
    def post(request):
        name = request.POST['name']
        desc = request.POST['desc']
        img = request.FILES['img']
        category_service.create(name, desc, img)
        return HttpResponseRedirect('/category/create')

    @staticmethod
    def get(request):
        return render(request, 'catalog/category/create.html')


class RetrieveCategory(View):
    @staticmethod
    def get(request):
        category_paginator = category_service.retrieve()
        page_obj = category_service.paginator(request, category_paginator)
        category, product = product_service.category_product()
        return render(request, 'catalog/category/retrieve.html', {'page_obj': page_obj, 'category': category,
                                                                  'product': product})


class UpdateCategory(View):
    @staticmethod
    def post(request, category_id: int):
        new_name = request.POST['name']
        new_desc = request.POST['desc']
        new_img = request.FILES['img']

        category_service.update(category_id, new_name, new_desc, new_img)
        return HttpResponseRedirect('/category/retrieve')

    @staticmethod
    def get(request, category_id: int):
        category = category_service.retrieve_id(category_id)
        return render(request, 'catalog/category/update.html', {'category': category})


class DeleteCategory(View):
    @staticmethod
    def get(request, category_id: int):
        category_service.delete(category_id)
        return HttpResponseRedirect('/category/retrieve')


class CreateProduct(View):
    @staticmethod
    def post(request):
        product_name = request.POST['name']
        product_desc = request.POST['desc']
        product_category = request.POST.getlist('category')
        product_images = request.FILES.getlist('img')
        product_service.create(product_name, product_desc, product_category, product_images)
        return HttpResponseRedirect('/product/create')

    @staticmethod
    def get(request):
        category = Category.objects.exclude(parent__isnull=False)
        return render(request, 'catalog/product/create.html', {'category': category})

# class retrieve_product_by_category(View):
#     def get(self, request, category):
#         product_paginator =  product = Product.objects.get(product_name=category)


class RetrieveProduct(View):
    @staticmethod
    def get(request):
        product_paginator = product_service.retrieve()
        page_obj = category_service.paginator(request, product_paginator)
        category, product = product_service.category_product()
        return render(request, 'catalog/product/retrieve.html', {'page_obj': page_obj, 'category': category,
                                                                 'product': product})


class UpdateProduct(View):
    @staticmethod
    def post(request, product_id: int):
        new_name = request.POST['name']
        new_desc = request.POST['desc']
        new_images = request.FILES.getlist('img')
        product_service.update(product_id, new_name, new_desc, new_images)
        return HttpResponseRedirect('/product/retrieve')

    @staticmethod
    def get(request, product_id: int):
        product = product_service.retrieve_id(product_id)
        return render(request, 'catalog/product/update.html', {'product_new': product})


class DeleteProduct(View):
    @staticmethod
    def get(request, product_id: int):
        product_service.delete(product_id)
        return HttpResponseRedirect('/product/retrieve')

