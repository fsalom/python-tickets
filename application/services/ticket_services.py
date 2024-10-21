from asgiref.sync import sync_to_async

from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from application.ports.driving.tickets_service_port import TicketServicePort
from domain.product import Product
from domain.ticket import Ticket


class TicketServices(TicketServicePort):
    def __init__(self,
                 db_repository: TicketDBRepositoryPort):
        self.db_repository = db_repository

    async def get_ticket_for_user(self, user: str) -> [Ticket]:
        return await self.db_repository.get_tickets_for(user)

    async def get_number_of_products_for(self, user: str, start_date: str, end_date: str) -> int:
        return await self.db_repository.get_number_of_products_for(user, start_date, end_date)

    async def get_number_of_tickets_for(self, user: str, start_date: str, end_date: str) -> int:
        return await self.db_repository.get_number_of_tickets_for(user, start_date, end_date)

    async def get_total_for(self, user: str, start_date: str, end_date: str) -> float:
        return await self.db_repository.get_total_for(user, start_date, end_date)

    async def get_top_products_for(self, user: str, start_date: str, end_date: str, number: int = 10) -> [Product]:
        return await self.db_repository.get_total_for(user, start_date, end_date)
