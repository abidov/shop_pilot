from django.db import models
from django.urls import reverse
from apps.categories.models import Category


PRODUCT_COLORS = (
    ('BLACK', 'Black'),
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('BROWN', 'Brown'),
    ('PURPLE', 'Purple'),
)



class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='product name')
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    color = models.CharField(choices=PRODUCT_COLORS, max_length=255, db_index=True)
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # 2000.00
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')

    def __str__(self):
        return f"{self.product.name}'s item"



class ProductItemImage(models.Model):
    image = models.ImageField(upload_to='productImages')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_item_images')

    def __str__(self):
        return f"{self.product_item.product.name}'s image"
