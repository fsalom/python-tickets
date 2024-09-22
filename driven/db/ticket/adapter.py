from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from domain.ticket import Ticket
from driven.db.product.models import ProductDBO
from driven.db.ticket.models import TicketDBO


class TicketDBRepositoryAdapter(TicketDBRepositoryPort):
    def __init__(self):
        print("")

    def save(self, ticket: Ticket):
        productsDBO = []
        for product in ticket.products:
            productsDBO.append(
                ProductDBO.objects.get_or_create(

                )
            )

        ticket_dbo = TicketDBO.objects.create(
            date=ticket.date,
            location=ticket.location,
            email=ticket.email,
            product=productsDBO
        )
