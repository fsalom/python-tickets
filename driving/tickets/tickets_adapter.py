from application.services.mail_services import TicketServices
from domain.ticket import Ticket


class TicketsDBAdapter:
    def __init__(self, ticket_service: TicketServices):
        self.tickets = []
        self.ticket_service = ticket_service

    def get_tickets(self, user_id: int) -> [Ticket]:
        return self.ticket_service.get(user_id)
