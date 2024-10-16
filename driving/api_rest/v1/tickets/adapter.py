from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from application.ports.driving.tickets_service_port import TicketServicePort
from driving.api_rest.v1.tickets.mapper import TicketDTOMapper
from infrastructure.di.tickets.container import TicketContainer
from application.services.ticket_services import TicketServices
from domain.user import User
from driving.api_rest.security import get_user_or_refuse

ticket_router = APIRouter()


@ticket_router.get('/tickets/all')
@inject
async def me(user: Annotated[User, Depends(get_user_or_refuse)],
             service: TicketServicePort = Depends(Provide[TicketContainer.service]),
             mapper: TicketDTOMapper = Depends(Provide[TicketContainer.mapper])):
    tickets = await service.get_ticket_for_user(user=user.email)
    return mapper.to_dto(tickets)


@ticket_router.get('/tickets/test')
@inject
async def me(service: TicketServices = Depends(Provide[TicketContainer.service])):
    tickets = await service.get_ticket_for_user(user="fdosalom@gmail.com")
    return {"num_tickets": len(tickets), "tickets": [ticket.__dict__ for ticket in tickets]}
