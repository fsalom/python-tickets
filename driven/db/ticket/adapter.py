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
        store_dbo = TicketDBMapper.map_store(ticket)
        user_dbo = TicketDBMapper.map_user(ticket)
        ticket_dbo = TicketDBMapper.map_ticket(ticket, store_dbo, user_dbo)
        products_dbo = TicketDBMapper.map_products_of_ticket(ticket_dbo, ticket.products, ticket.date)
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
