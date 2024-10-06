from django.db import models
from django.utils.timezone import now


class ProductDBO(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class ProductPriceHistoryDBO(models.Model):
    product = models.ForeignKey(ProductDBO, verbose_name="Product", on_delete=models.CASCADE, related_name='price_history')
    created_at = models.DateTimeField(auto_now_add=True)
    date_raw = models.CharField(max_length=25)
    price = models.FloatField(verbose_name="Price")
    price_per_unit = models.FloatField(verbose_name="Price per Unit")

    def __str__(self):
        return f"{self.price}€"

    class Meta:
        verbose_name = "Relación historia precio producto"
        verbose_name_plural = "Relación historia precio productos"
