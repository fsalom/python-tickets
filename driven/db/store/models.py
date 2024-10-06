from django.db import models


class StoreDBO(models.Model):
    location_info = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.location_info}"

    class Meta:
        verbose_name = "Localización"
        verbose_name_plural = "Localizaciones"