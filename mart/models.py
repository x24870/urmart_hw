from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Shop(models.Model):
    shop_id = models.CharField(max_length=50)

    def __str__(self):
        return self.shop_id

class Product(models.Model):
    stock_pcs = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shop_id = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    vip_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def customer(self):
        return self.customer.id

    @property
    def price(self):
        return self.product.price

    @property
    def shop_id(self):
        return self.product.shop_id