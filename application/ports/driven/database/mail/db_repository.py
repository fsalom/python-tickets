from abc import ABC, abstractmethod


class MailDBRepositoryPort(ABC):
    @abstractmethod
    def save(self, mail: str):
        pass
