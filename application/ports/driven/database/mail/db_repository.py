from abc import ABC, abstractmethod

from domain.mail import Mail


class MailDBRepositoryPort(ABC):
    @abstractmethod
    def save(self, mail: Mail):
        pass
