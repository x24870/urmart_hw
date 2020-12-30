from django.db import models

class OrderManager(models.Manager):
    def create_order(self, customer, product, quantity):
        new_order = self.model(customer=customer, product=product, quantity=quantity)
        new_order.save()
        product.stock_pcs -= int(quantity)
        product.save()

        return new_order

    def delete(self):
        print(self)
