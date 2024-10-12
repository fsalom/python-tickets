from dependency_injector import containers, providers

from application.services.authentication_services import AuthenticationServices
from driven.db.authentication.adapter import AuthenticationDBRepositoryAdapter


class AuthenticationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    #wiring_config = containers.WiringConfiguration(modules=["poc.di.driving.api_rest.adapters.example_controller_adapter"])

    service = providers.Factory(
        AuthenticationServices,
        db_repository=AuthenticationDBRepositoryAdapter()
    )
