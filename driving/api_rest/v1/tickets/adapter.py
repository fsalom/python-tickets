from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query

from application.ports.driving.tickets_service_port import TicketServicePort
from driving.api_rest.v1.tickets.mapper import TicketDTOMapper
from driving.api_rest.v1.tickets.models import StatsForTicketsResponse
from infrastructure.di.tickets.container import TicketContainer
from application.services.ticket_services import TicketServices
from domain.user import User
from driving.api_rest.security import get_user_or_refuse

ticket_router = APIRouter()


@ticket_router.get('/tickets/all')
@inject
async def me(user: Annotated[User, Depends(get_user_or_refuse)],
             service: TicketServicePort = Depends(Provide[TicketContainer.service]),
             api_mapper: TicketDTOMapper = Depends(Provide[TicketContainer.api_mapper])):
    tickets = await service.get_ticket_for_user(user=user.email)
    return api_mapper.to_dto(tickets)


@ticket_router.get('/tickets/stats')
@inject
async def stats(user: Annotated[User, Depends(get_user_or_refuse)],
                service: TicketServicePort = Depends(Provide[TicketContainer.service]),
                api_mapper: TicketDTOMapper = Depends(Provide[TicketContainer.api_mapper]),
                start_date: str = Query(..., description="Start date in format YYYY-MM-DD"),
                end_date: str = Query(..., description="End date in format YYYY-MM-DD")):
    total = await service.get_total_for(user=user.email, start_date=start_date, end_date=end_date)
    num_tickets = await service.get_number_of_tickets_for(user=user.email, start_date=start_date, end_date=end_date)
    num_products = await service.get_number_of_products_for(user=user.email, start_date=start_date, end_date=end_date)
    top_products = await service.get_top_products_for(user=user.email, start_date=start_date, end_date=end_date)
    top_products_dto = api_mapper.products_to_dto(top_products)

    return StatsForTicketsResponse(total=total,
                                   num_tickets=num_tickets,
                                   num_products=num_products,
                                   top_products=top_products_dto)


@ticket_router.get('/tickets/test')
@inject
async def me(service: TicketServices = Depends(Provide[TicketContainer.service])):
    tickets = await service.get_ticket_for_user(user="fdosalom@gmail.com")
    return {"num_tickets": len(tickets), "tickets": [ticket.__dict__ for ticket in tickets]}
