from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from application.ports.driving.tickets_service_port import TicketServicePort
from infrastructure.di.tickets.container import TicketContainer
from infrastructure.di.tickets.injector import TicketInjector
from application.services.ticket_services import TicketServices
from domain.user import User
from driving.api_rest.security.security import get_user_or_refuse

ticket_router = APIRouter()


@ticket_router.get('/tickets/all')
@inject
async def me(user: Annotated[User, Depends(get_user_or_refuse)],
             service: TicketServicePort = Depends(Provide[TicketContainer.service])):
    tickets = await service.get_ticket_for_user(user=user.email)
    return {"num_tickets": len(tickets), "tickets": [ticket.__dict__ for ticket in tickets]}


@ticket_router.get('/tickets/test')
@inject
async def me(service: TicketServices = Depends(Provide[TicketContainer.service])):
    tickets = await service.get_ticket_for_user(user="fdosalom@gmail.com")
    return {"num_tickets": len(tickets), "tickets": [ticket.__dict__ for ticket in tickets]}
