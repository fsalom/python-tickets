# driven/db/user/apps.py
from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'driven.db.user'  # Ruta completa al módulo
    label = 'user'  # Esto define el "app_label" que se usará para referenciar este modelo
