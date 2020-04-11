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

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('product-detail', kwargs = {"pk" : self.pk})

=======
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19

class InStockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(quantity=0)


class ProductItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class ProductItem(models.Model):
<<<<<<< HEAD
    color = models.CharField(choices=PRODUCT_COLORS, max_length=255, db_index=True, default=('PURPLE', 'Purple'))
=======
    color = models.CharField(choices=PRODUCT_COLORS, max_length=255, db_index=True)
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # 2000.00
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')

    def __str__(self):
        return f"{self.product.name}'s item"
<<<<<<< HEAD

    def get_absolute_url(self):
        return reverse('productitem-detail', kwargs = {'pk' : self.pk})
    
    objects = ProductItemManager()
    instock = InStockManager()
    
    
    
=======
    
    instock = InStockManager()
    objects = ProductItemManager()
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19



class ProductItemImage(models.Model):
    image = models.ImageField(upload_to='productImages')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_item_images')

    def __str__(self):
        return f"{self.product_item.product.name}'s image"
