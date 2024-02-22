from django.db import models
from.product import Product
from.user import CustomUser


class Order(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='a')
    product = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='b')
    quantity =models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
