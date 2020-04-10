from rest_framework import serializers
from django.contrib.auth.models import User

from apps.products.serializers import ProductItemSerializer
from .models import Bookmark


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'bookmark', 'cart')



class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItemSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ('user', 'product_items')