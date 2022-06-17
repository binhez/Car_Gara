from django.urls import path
from . import views

app_name = 'catalog_app'
urlpatterns = [
    path('', views.home, name="home"),
    path('brand/', views.brand, name="brand"),
    path('contact/', views.contact, name="contact"),

    path('category/create', views.create_category.as_view(), name ="create_category"),
    path('category/retrieve', views.retrieve_category.as_view(), name="retrieve_category"),
    path('category/update/<int:id>', views.update_category.as_view(), name="update_category"),
    path('category/delete/<int:id>', views.delete_category.as_view(), name="delete_category"),

    path('product/create', views.create_product.as_view(), name="create_product"),
    path('product/retrieve', views.retrieve_product.as_view(), name="retrieve_product"),
    path('product/update/<int:id>', views.update_product.as_view(), name="update_product"),
    path('product/delete/<int:id>', views.delete_product.as_view(), name="delete_product"),
]
