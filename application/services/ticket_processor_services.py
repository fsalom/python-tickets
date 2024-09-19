from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from application.ports.driving.tickets_service_port import TicketServicePort
from domain.ticket import Ticket


class TicketProcessorServices(TicketServicePort):
    def __init__(self,
                 db_repository: TicketDBRepositoryPort):
        self.db_repository = db_repository

    def process(self, ticket: Ticket):
        self.db_repository.save(ticket)
