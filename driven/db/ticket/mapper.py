from domain.product import Product
from domain.ticket import Ticket
from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO
from driven.db.store.models import StoreDBO
from driven.db.ticket.models import TicketDBO
from driven.db.user.models import UserDBO


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

    @staticmethod
    def map_store(ticket: Ticket) -> StoreDBO:
        store_dbo, _ = StoreDBO.objects.get_or_create(
            location_info=ticket.location
        )
        return store_dbo

    @staticmethod
    def map_user(ticket: Ticket) -> UserDBO:
        user_dbo, _ = UserDBO.objects.get_or_create(
            email=ticket.email,
            username=ticket.email
        )
        return user_dbo

    @staticmethod
    def map_product(product: Product, date: str) -> (ProductDBO, ProductPriceHistoryDBO):
        product_dbo, _ = ProductDBO.objects.get_or_create(
            name=product.name
        )
        product_history_price, _ = ProductPriceHistoryDBO.objects.get_or_create(
            product=product_dbo,
            date_raw=date,
            price=product.price,
            price_per_unit=product.price_per_unit
        )
        return product_dbo, product_history_price

    @staticmethod
    def map_ticket(ticket: Ticket, store_dbo: StoreDBO, user_dbo: UserDBO) -> TicketDBO:
        ticket_dbo, _ = TicketDBO.objects.get_or_create(
            date_raw=ticket.date,
            location=store_dbo,
            email=user_dbo,
            total=ticket.total,
            id_ticket=ticket.id
        )
        return ticket_dbo
