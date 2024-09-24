from django.contrib import admin
from driven.db.store.models import StoreDBO


class StoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoreDBO, StoreAdmin)
