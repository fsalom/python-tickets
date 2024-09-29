from abc import ABC, abstractmethod

from domain.ticket import Ticket


class TicketDBRepositoryPort(ABC):
    @abstractmethod
    def save(self, ticket: Ticket):
        pass

    @abstractmethod
    async def get_tickets_for(self, user: str) -> [Ticket]:
        pass
