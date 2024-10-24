from asgiref.sync import sync_to_async
from django.forms import models

from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from domain.product import Product
from domain.ticket import Ticket
from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO
from driven.db.store.models import StoreDBO
from driven.db.ticket.mapper import TicketDBMapper
from driven.db.ticket.models import TicketDBO, TicketProductDBO
from driven.db.user.models import UserDBO


class TicketDBRepositoryAdapter(TicketDBRepositoryPort):
    def __init__(self, mapper: TicketDBMapper):
        self.mapper = mapper

    def save(self, ticket: Ticket):
        store_dbo = TicketDBMapper.map_store(ticket)
        user_dbo = TicketDBMapper.map_user(ticket)
        ticket_dbo = TicketDBMapper.map_ticket(ticket, store_dbo, user_dbo)
        products_dbo = TicketDBMapper.map_products_of_ticket(ticket_dbo, ticket.products, ticket.date)
        ticket_dbo.products.set(products_dbo)

    async def get_tickets_for(self, user: str) -> [Ticket]:
        def _get_tickets(current_user) -> [Ticket]:
            ticket_dbo_list = TicketDBO.objects.filter(email__email=current_user)
            return TicketDBMapper.to_dbos(ticket_dbo_list)

        tickets = await sync_to_async(_get_tickets)(user)
        return tickets

    async def get_total_for(self, user: str, start_date: str, end_date: str) -> float:
        def _get_total(current_user, start_date, end_date) -> float:
            tickets = TicketDBO.objects.filter(
                email__email=current_user,
                date_raw__gte=start_date,
                date_raw__lte=end_date
            )
            return tickets.aggregate(total=models.Sum('total'))['total'] or 0.0

        total = await sync_to_async(_get_total)(user, start_date, end_date)
        return total

    async def get_number_of_tickets_for(self, user: str, start_date: str, end_date: str) -> int:
        def _get_ticket_count(current_user, start_date, end_date) -> int:
            return TicketDBO.objects.filter(
                email__email=current_user,
                date_raw__gte=start_date,
                date_raw__lte=end_date
            ).count()

        count = await sync_to_async(_get_ticket_count)(user, start_date, end_date)
        return count

    async def get_number_of_products_for(self, user: str, start_date: str, end_date: str) -> int:
        def _get_product_count(current_user, start_date, end_date) -> int:
            tickets = TicketDBO.objects.filter(
                email__email=current_user,
                date_raw__gte=start_date,
                date_raw__lte=end_date
            )
            return TicketProductDBO.objects.filter(ticket__in=tickets).aggregate(
                total_quantity=models.Sum('quantity')
            )['total_quantity'] or 0

        count = await sync_to_async(_get_product_count)(user, start_date, end_date)
        return count

    async def get_top_products_for(self, user: str, start_date: str, end_date: str, number: int = 10) -> [Product]:
        def _get_top_products(current_user, start_date, end_date, number) -> [Product]:
            tickets = TicketDBO.objects.filter(
                email__email=current_user,
                date_raw__gte=start_date,
                date_raw__lte=end_date
            )
            top_products = TicketProductDBO.objects.filter(ticket__in=tickets).values(
                'product__name'
            ).annotate(total_quantity=models.Sum('quantity')).order_by('-total_quantity')[:number]

            return [
                Product(name=prod['product__name'], quantity=prod['total_quantity'])
                for prod in top_products
            ]

        top_products = await sync_to_async(_get_top_products)(user, start_date, end_date, number)
        return top_products
