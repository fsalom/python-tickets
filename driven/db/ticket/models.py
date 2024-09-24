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

    def __str__(self):
        return f"Ticket {self.id}"


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
