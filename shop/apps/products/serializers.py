from rest_framework import serializers
from .models import Product, ProductItem, ProductItemImage


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'description', 'categories')


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
<<<<<<< HEAD
    product_items = ProductItem.instock.all()
=======

>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
    class Meta:
        model = Product
        fields = ('name', 'description', 'product_items', 'categories')


class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = ('url', 'color', 'size', 'quantity', 'price', 'product', 'product_item_images')


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductItemImage
        fields = ('product_item', 'image',)