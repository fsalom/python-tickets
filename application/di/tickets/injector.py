from application.services.ticket_services import TicketServices
from driven.db.ticket.adapter import TicketDBRepositoryAdapter


class TicketInjector:
    def __init__(self):
        self.db_repository = TicketDBRepositoryAdapter()

    def get_service(self):
        db_repository = self.db_repository
        return TicketServices(db_repository=db_repository)
