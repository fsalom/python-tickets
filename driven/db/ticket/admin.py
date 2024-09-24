from django.contrib import admin
from .models import TicketDBO, TicketProductDBO


class TicketProductInline(admin.TabularInline):
    model = TicketProductDBO
    extra = 0
    readonly_fields = ('product', 'quantity', 'history_price', 'units')


@admin.register(TicketDBO)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'location', 'email', 'total')
    inlines = [TicketProductInline]


@admin.register(TicketProductDBO)
class TicketProductAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'product', 'quantity', 'history_price', 'units')
