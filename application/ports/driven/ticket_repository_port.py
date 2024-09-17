from abc import ABC, abstractmethod
from domain.ticket import Ticket


class TicketRepositoryPort(ABC):
    @abstractmethod
    def get(self, mail: str) -> [Ticket]:
        pass

    @abstractmethod
    def get(self, mail: str) -> [Ticket]:
        pass