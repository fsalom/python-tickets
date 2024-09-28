from application.services.authentication_services import AuthenticationServices
from driven.db.authentication.adapter import AuthenticationDBRepositoryAdapter


class AuthenticationInjector:
    def __init__(self):
        self.db_repository = AuthenticationDBRepositoryAdapter()

    def get_authentication_service(self):
        def get_service():
            db_repository = self.db_repository
            return AuthenticationServices(db_repository=db_repository)

        return get_service
