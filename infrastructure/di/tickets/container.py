from dependency_injector import containers, providers

from application.services.ticket_services import TicketServices
from driven.db.ticket.adapter import TicketDBRepositoryAdapter
from driving.api_rest.v1.tickets.mapper import TicketDTOMapper


class TicketContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.api_rest.v1.tickets.adapter"])

    db_repository = providers.Factory(TicketDBRepositoryAdapter)

    service = providers.Factory(
        TicketServices,
        db_repository=db_repository
    )

    mapper = providers.Factory(
        TicketDTOMapper
    )
