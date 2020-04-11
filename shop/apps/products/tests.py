<<<<<<< HEAD
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, ProductItem


class ProductTest(APITestCase):
    def setUp(self):
        # user = User.objects.create(username = 'tester', email = 'tester@mail.ru')
        # user.set_password('Aidar3008!')
        # user.save()
        product = Product.objects.create(name = 'Jeans', description = 'Long_stylish')
        product_item = ProductItem.objects.create(color = 'Blue', size = 40, quantity = 3, price = 1000, product = product)   
    def test_get_product_list(self):
        url = reverse('product-list')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def test_get_product_detail(self):
        product = Product.objects.first()
        url = product.get_absolute_url()
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def test_get_product_item_detail(self):
        product_item = ProductItem.objects.first()
        url = product_item.get_absolute_url()
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def 
        
        




=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
