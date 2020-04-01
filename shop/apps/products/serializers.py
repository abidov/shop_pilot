from rest_framework import serializers
from .models import Product, ProductItem, ProductItemImage


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'description')


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'product_items')


class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = ('color', 'size', 'quantity', 'price', 'product')