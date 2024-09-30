from asgiref.sync import sync_to_async

from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from application.ports.driving.tickets_service_port import TicketServicePort
from domain.ticket import Ticket


class TicketServices(TicketServicePort):
    def __init__(self,
                 db_repository: TicketDBRepositoryPort):
        self.db_repository = db_repository

    async def get_ticket_for_user(self, user: str) -> [Ticket]:
        return await self.db_repository.get_tickets_for(user)
