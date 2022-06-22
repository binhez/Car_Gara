from rest_framework import serializers
from catalog.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_date', 'updated_date', 'category_image', 'parent']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['img']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'created_date', 'updated_date', 'category', 'product_image']


class ProductCommentsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductComments
        fields = ['product_id', 'product', 'comments']


class TotalProductsSerializer(serializers.Serializer):  # noqa
    total = serializers.IntegerField()
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Category
        fields = ['name', 'total']
