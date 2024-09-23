from django.db import models


class ProductDBO(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    quantity = models.IntegerField(verbose_name="Quantity")

    def __str__(self):
        return self.name


class ProductPriceHistoryDBO(models.Model):
    product = models.ForeignKey(ProductDBO, verbose_name="Product", on_delete=models.CASCADE, related_name='price_history')
    created_at = models.DateTimeField(auto_now_add=True)
    date_raw = models.CharField(max_length=25)
    price = models.FloatField(verbose_name="Price")
    price_per_unit = models.FloatField(verbose_name="Price per Unit")
    quantity = models.IntegerField(verbose_name="Quantity")

    def __str__(self):
        return f"{self.product.name} - {self.price} - {self.date_raw}"
