from application.ports.driven.database.user.db_repository import UserDBRepositoryPort
from domain.user import User


class UserDBRepositoryAdapter(UserDBRepositoryPort):
    def get(self, user: str) -> User:
        pass
