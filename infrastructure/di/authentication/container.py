from dependency_injector import containers, providers
from fastapi.security import OAuth2PasswordBearer

from application.services.authentication_services import AuthenticationServices
from driven.db.authentication.adapter import AuthenticationDBRepositoryAdapter


class AuthenticationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.api_rest.security",
                                                            "driving.api_rest.v1.authentication.adapter"])
    db_repository = providers.Factory(AuthenticationDBRepositoryAdapter)
    oauth2_scheme = providers.Singleton(OAuth2PasswordBearer, tokenUrl="token")

    service = providers.Factory(
        AuthenticationServices,
        db_repository=db_repository
    )
