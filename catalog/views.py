import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import *
from catalog.service import category_service, product_service


# Create your views here.
@login_required(login_url='user_app:login')
def home(request):
    category, product = product_service.category_product()
    return render(request, 'catalog/index.html', {'category': category, 'product': product})

def brand(request):
    return render(request, 'catalog/brand.html')

def contact(request):
    return render(request, 'catalog/contact.html')


class create_category(View):
    def post(self, request):
        name = request.POST['name']
        desc = request.POST['desc']
        img = request.FILES['img']
        category_service.create(name, desc, img)
        return HttpResponseRedirect('/category/create')

    def get(self, request):
        return render(request, 'catalog/category/create.html')


class retrieve_category(View):
    def get(self, request):
        category = category_service.retrieve()
        page_obj = category_service.paginator(request, category)
        return render(request, 'catalog/category/retrieve.html', {'page_obj' : page_obj})


class update_category(View):
    def post(self, request, id):
        newname = request.POST['name']
        newdesc = request.POST['desc']
        newimg = request.FILES['img']

        category_service.update(id, newname, newdesc, newimg)
        return HttpResponseRedirect('/category/retrieve')

    def get(self, request, id):
        category = category_service.retrieve_id(id)
        return render(request, 'catalog/category/update.html', {'category': category})

class delete_category(View):
    def get(self,request, id):
        category_service.delete(id)
        return HttpResponseRedirect('/category/retrieve')

class create_product(View):
    def post(self, request):
        name = request.POST['name']
        desc = request.POST['desc']
        category = request.POST.getlist('category')
        images = request.FILES.getlist('img')
        product_service.create(name, desc, category, images)
        return HttpResponseRedirect('/product/create')
    def get(self, request):
        category = Category.objects.exclude(parent__isnull=False)
        return render(request, 'catalog/product/create.html', {'category': category})


class retrieve_product(View):
    def get(self, request):
        product = product_service.retrieve()
        page_obj = category_service.paginator(request, product)
        return render(request, 'catalog/product/retrieve.html', {'page_obj' : page_obj})

class update_product(View):
    def post(self, request, id):
        newname = request.POST['name']
        newdesc = request.POST['desc']
        newimgs = request.FILES.getlist('img')
        product_service.update(id, newname, newdesc, newimgs)
        return HttpResponseRedirect('/product/retrieve')
    def get(self, request, id):
        product = product_service.retrieve_id(id)
        return render(request, 'catalog/product/update.html', {'product_new': product})


class delete_product(View):
    def get(self,request, id):
        product_service.delete(id)
        return HttpResponseRedirect('/product/retrieve')
