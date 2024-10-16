from domain.ticket import Ticket
from driving.api_rest.v1.tickets.models import AllTicketsResponse, TicketResponse, ProductResponse


class TicketDTOMapper:

    @staticmethod
    def to_dto(tickets: [Ticket]) -> AllTicketsResponse:
        return AllTicketsResponse(
            num_tickets=len(tickets),
            tickets=[
                TicketResponse(
                    id_ticket=ticket.id,
                    products=[ProductResponse(**vars(product)) for product in ticket.products],
                    total=ticket.total,
                    iva=ticket.iva,
                    date=ticket.date,
                    email=ticket.email,
                    location=ticket.location
                ) for ticket in tickets
            ])
