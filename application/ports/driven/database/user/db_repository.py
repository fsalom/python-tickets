from abc import ABC, abstractmethod

from domain.user import User


class UserDBRepositoryPort(ABC):
    @abstractmethod
    def get(self, user: str) -> User:
        pass
