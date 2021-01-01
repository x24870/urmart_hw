from django.db import models
from django.conf import settings

from .managers import OrderManager

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Shop(models.Model):
    shop_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.shop_id)

class Product(models.Model):
    stock_pcs = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shop_id = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    vip_only = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    objects = OrderManager()

    @property
    def price(self):
        return str(self.product.price)

    @property
    def total_price(self):
        return str(int(self.product.price) * self.quantity)

    @property
    def shop_id(self):
        return str(self.product.shop_id)

    def __str__(self):
        return str(self.id)