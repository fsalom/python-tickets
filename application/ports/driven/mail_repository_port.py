from abc import ABC, abstractmethod

from domain.mail import Mail


class MailRepositoryPort(ABC):
    @abstractmethod
    def read(self) -> [Mail]:
        pass
