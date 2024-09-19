from django.db import models

from domain.product import Product
from driven.db.user.models import User


class Ticket(models.Model):
    date = models.DateField(auto_now_add=True)
    quantity = models.CharField(max_length=2)
    products = models.ManyToManyField(Product)
    place = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner"
    )
