from abc import ABC, abstractmethod

from domain.ticket import Ticket


class TicketServicePort(ABC):
    @abstractmethod
    async def get_ticket_for_user(self, user: str) -> [Ticket]:
        pass
