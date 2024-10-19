from domain.product import Product
from domain.ticket import Ticket
from driven.db.ticket.models import TicketDBO


class TicketDBMapper:

    @staticmethod
    def to_dbos(tickets_dbo_list: [TicketDBO]) -> [Ticket]:
        tickets = []
        for ticket_dbo in tickets_dbo_list:
            products = [
                Product(
                    name=ticket_product_dbo.product.name,
                    quantity=ticket_product_dbo.quantity,
                    price_per_unit=ticket_product_dbo.history_price.price_per_unit,
                    price=ticket_product_dbo.history_price.price,
                    weight=None
                )
                for ticket_product_dbo in ticket_dbo.ticket_products.all()
            ]
            tickets.append(
                Ticket(
                    id_ticket=ticket_dbo.id_ticket,
                    products=products,
                    total=ticket_dbo.total,
                    iva=0.0,
                    date=str(ticket_dbo.date_raw),
                    email=ticket_dbo.email.email,
                    location=ticket_dbo.location.location_info,
                )
            )
        return tickets
