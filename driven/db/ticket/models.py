from datetime import datetime

from django.db import models

from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO
from driven.db.store.models import StoreDBO
from driven.db.user.models import UserDBO


class TicketDBO(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_raw = models.CharField(max_length=25)
    location = models.ForeignKey(
        StoreDBO, on_delete=models.CASCADE, related_name="ticket_locations"
    )
    products = models.ManyToManyField(
        ProductDBO, through='TicketProductDBO'
    )
    email = models.ForeignKey(
        UserDBO, on_delete=models.CASCADE, related_name="tickets"
    )
    total = models.FloatField()
    id_ticket = models.CharField(max_length=50, unique=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.date_raw:
            try:
                parsed_datetime = datetime.strptime(self.date_raw, '%d/%m/%Y %H:%M')
                self.date = parsed_datetime.date()
                self.time = parsed_datetime.time()
            except ValueError:
                raise ValueError(f"Formato de date_raw incorrecto: {self.date_raw}")

        super(TicketDBO, self).save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.id}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


class TicketProductDBO(models.Model):
    ticket = models.ForeignKey(
        TicketDBO, on_delete=models.CASCADE, related_name="ticket_products"
    )
    product = models.ForeignKey(
        ProductDBO, on_delete=models.CASCADE, related_name="product_tickets"
    )
    quantity = models.FloatField(default=0)
    history_price = models.ForeignKey(
        ProductPriceHistoryDBO, on_delete=models.CASCADE, related_name="ticket_price"
    )
    units = models.FloatField(default=1)

    def __str__(self):
        return f"Ticket {self.ticket.id} - {self.product.name} - Qty: {self.quantity} - Price: {self.history_price.price}"

    class Meta:
        verbose_name = "Producto del ticket"
        verbose_name_plural = "Productos de los tickets"