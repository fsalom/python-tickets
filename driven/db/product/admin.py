from django.contrib import admin
from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductDBO, ProductAdmin)
admin.site.register(ProductPriceHistoryDBO, ProductAdmin)