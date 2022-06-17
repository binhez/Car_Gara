from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .auth import account
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View

# Create your views here.
class login_page(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = account._login(username=username, password=password)
        state = False
        if user is not None:
            login(request,user=user)
            state = True
        if state == True:
            return redirect('catalog_app:home')
        else:
            messages.warning(request, 'Username OR password is incorrect')
            return HttpResponseRedirect('/login')
    def get(self, request):
        return render(request, 'account/index.html')

class signup_page(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        state = account._signup(username, email, password)
        if state is True:
            messages.success(request, "Create new user successfully")
            return redirect('user_app:login')
        else:
            messages.error(request, "User is already exist")
            return redirect('user_app:signup')
    def get(self, request):
        return render(request, 'account/signup.html')

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         state = account._login(username=username, password=password)
#         if state == True:
#             return redirect('catalog_app:home')
#         else:
#             messages.warning(request,'Username OR password is incorrect')
#     return render(request, 'account/index.html')

# def signup_page(request):
#     state = account._signup(request)
#     if state is True:
#         return redirect('user_app:login')
#     return render(request, 'account/signup.html')

class logoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('catalog_app:home')
