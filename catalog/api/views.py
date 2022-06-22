from django.db.models import Count, Prefetch
from rest_framework import generics
from catalog.models import *
from .serializiers import (
    CategorySerializer,
    ProductSerializer,
    TotalProductsSerializer,
    ProductCommentsSerializer
    )


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TotalProductsView(generics.ListAPIView):
    queryset = Category.objects.values('name').annotate(total=Count('c_products'))
    serializer_class = TotalProductsSerializer


class ProductCommentsView(generics.RetrieveAPIView):
    serializer_class = ProductCommentsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        comment_object, _ = ProductComments.objects.get_or_create(product_id=pk)
        qs = ProductComments.objects.filter(product_id=pk)
        return qs


class AddProductCommentsView(generics.CreateAPIView):
    serializer_class = ProductCommentsSerializer

