from abc import ABC, abstractmethod

from domain.product import Product
from domain.ticket import Ticket


class TicketServicePort(ABC):
    @abstractmethod
    async def get_ticket_for_user(self, user: str) -> [Ticket]:
        pass

    @abstractmethod
    async def get_total_for(self, user: str, start_date: str, end_date: str) -> float:
        pass

    @abstractmethod
    async def get_number_of_tickets_for(self, user: str, start_date: str, end_date: str) -> int:
        pass

    @abstractmethod
    async def get_number_of_products_for(self, user: str, start_date: str, end_date: str) -> int:
        pass

    @abstractmethod
    async def get_top_products_for(self, user: str, start_date: str, end_date: str, number: int = 10) -> [Product]:
        pass
