from asgiref.sync import sync_to_async

from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from domain.product import Product
from domain.ticket import Ticket
from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO
from driven.db.store.models import StoreDBO
from driven.db.ticket.mapper import TicketDBMapper
from driven.db.ticket.models import TicketDBO, TicketProductDBO
from driven.db.user.models import UserDBO


class TicketDBRepositoryAdapter(TicketDBRepositoryPort):
    def __init__(self, mapper: TicketDBMapper):
        self.mapper = mapper

    def save(self, ticket: Ticket):
        products_dbo = []

        store_dbo, created = StoreDBO.objects.get_or_create(
            location_info=ticket.location
        )

        user_dbo, created = UserDBO.objects.get_or_create(
            email=ticket.email,
            username=ticket.email
        )

        ticket_dbo, created = TicketDBO.objects.get_or_create(
            date_raw=ticket.date,
            location=store_dbo,
            email=user_dbo,
            total=ticket.total,
            id_ticket=ticket.id
        )

        for product in ticket.products:
            product_dbo, created = ProductDBO.objects.get_or_create(
                name=product.name
            )

            product_history_price, created = ProductPriceHistoryDBO.objects.get_or_create(
                product=product_dbo,
                date_raw=ticket.date,
                price=product.price,
                price_per_unit=product.price_per_unit
            )

            TicketProductDBO.objects.create(
                ticket=ticket_dbo,
                product=product_dbo,
                quantity=product.quantity,
                history_price=product_history_price,
                units=product.price_per_unit
            )

            products_dbo.append(product_dbo)

        ticket_dbo.products.set(products_dbo)

    async def get_tickets_for(self, user: str) -> [Ticket]:
        def _get_tickets(current_user) -> [Ticket]:
            ticket_dbo_list = TicketDBO.objects.filter(email__email=current_user)
            return TicketDBMapper.to_dbos(ticket_dbo_list)

        tickets = await sync_to_async(_get_tickets)(user)
        return tickets

    async def get_total_for(self, user: str, start_date: str, end_date: str) -> float:
        pass

    async def get_number_of_tickets_for(self, user: str, start_date: str, end_date: str) -> int:
        pass

    async def get_number_of_products_for(self, user: str, start_date: str, end_date: str) -> int:
        pass

    async def get_top_products_for(self, user: str, start_date: str, end_date: str, number: int = 10) -> [Product]:
        pass
