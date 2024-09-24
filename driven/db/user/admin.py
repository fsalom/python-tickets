from django.contrib import admin
from driven.db.user.models import UserDBO


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserDBO, UserAdmin)
