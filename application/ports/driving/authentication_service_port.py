from abc import ABC, abstractmethod

from domain.tokens import Tokens
from domain.user import User


class AuthenticationServicePort(ABC):
    @abstractmethod
    def login(self, username: str, password: str, client_id: str) -> Tokens | None:
        pass

    @abstractmethod
    def get_user(self, token: str) -> User | None:
        pass