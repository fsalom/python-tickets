from django.db import models


class StoreDBO(models.Model):
    location_info = models.CharField(max_length=255)