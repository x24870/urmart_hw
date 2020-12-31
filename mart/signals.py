from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Order, Product

@receiver(pre_delete, sender=Order)
def pre_delete_order(sender, instance, **kwargs):
    '''
    Move the product in order back to stock.
    '''
    product = instance.product
    product.stock_pcs += instance.quantity
    product.save()