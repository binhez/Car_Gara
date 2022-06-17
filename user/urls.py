from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'user_app'
urlpatterns = [
    path('login/', views.login_page.as_view(), name="login"),
    path('signup/', views.signup_page.as_view(), name="signup"),
    path('logout/', views.logoutUser.as_view(), name='logout'),
]
