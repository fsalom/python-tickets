from dependency_injector import containers, providers

from application.services.authentication_services import AuthenticationServices
from driven.db.authentication.adapter import AuthenticationDBRepositoryAdapter


class AuthenticationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.api_rest.security.security",
                                                            "driving.api_rest.v1.authentication.adapter"])
    db_repository = providers.Singleton(AuthenticationDBRepositoryAdapter)

    service = providers.Factory(
        AuthenticationServices,
        db_repository=db_repository
    )
