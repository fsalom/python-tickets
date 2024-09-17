from abc import ABC, abstractmethod

from domain.ticket import Ticket


class TicketServicePort(ABC):
    @abstractmethod
    def process(self) -> [Ticket]:
        pass
