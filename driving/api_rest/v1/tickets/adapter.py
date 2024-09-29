from typing import Annotated

from asgiref.sync import sync_to_async
from fastapi import APIRouter, Depends

from application.di.tickets.injector import TicketInjector
from application.services.ticket_services import TicketServices
from domain.user import User
from driving.api_rest.security.security import get_user_or_refuse

ticket_router = APIRouter()


@ticket_router.get('/tickets/all')
async def me(user: Annotated[User, Depends(get_user_or_refuse)],
             service: TicketServices = Depends(TicketInjector().get_service)):
    tickets = await service.get_ticket_for_user(user=user.email)
    return {"num_tickets": len(tickets), "tickets": [ticket.__dict__ for ticket in tickets]}
