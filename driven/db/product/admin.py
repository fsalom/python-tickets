from django.contrib import admin
from driven.db.product.models import ProductDBO


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductDBO, ProductAdmin)