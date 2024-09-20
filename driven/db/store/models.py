from django.db import models


class StoreDBO(models.Model):
    location = models.CharField(max_length=50)
