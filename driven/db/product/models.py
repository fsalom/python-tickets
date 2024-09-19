from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    image = models.ImageField(verbose_name="Image", upload_to='products')
    price = models.FloatField(verbose_name="Price")
    quantity = models.IntegerField(verbose_name="Quantity")
