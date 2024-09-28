from abc import ABC, abstractmethod

from domain.tokens import Tokens


class AuthenticationDBRepositoryPort(ABC):
    @abstractmethod
    def login(self, username: str, password: str, client_id: str) -> Tokens | None:
        pass

    @abstractmethod
    def logout(self):
        pass
