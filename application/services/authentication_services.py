from asgiref.sync import sync_to_async

from application.ports.driven.database.authentication.db_repository import AuthenticationDBRepositoryPort
from application.ports.driving.authentication_service_port import AuthenticationServicePort
from domain.tokens import Tokens
from domain.user import User


class AuthenticationServices(AuthenticationServicePort):

    def __init__(self,
                 db_repository: AuthenticationDBRepositoryPort):
        self.db_repository = db_repository

    def login(self, username: str, password: str, client_id: str) -> Tokens | None:
        return self.db_repository.login(username, password, client_id)

    def get_user(self, token: str) -> User | None:
        user = self.db_repository.get_user(token)
        return user
