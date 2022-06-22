from . import views
from django.urls import path


# router = routers.DefaultRouter()
# router.register(r'category', views.CategoryViewSet)
# router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('categories/', views.CategoriesView.as_view(), name="category-detail"),
    path('categories/totalproducts/', views.TotalProductsView.as_view(), name='total-product-each-category'),

    path('products/', views.ProductsView.as_view(), name="product-detail"),
    path('comments/<int:pk>/', views.ProductCommentsView.as_view(), name="comments"),
]
