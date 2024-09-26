from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from domain.ticket import Ticket
from driven.db.product.models import ProductDBO, ProductPriceHistoryDBO
from driven.db.store.models import StoreDBO
from driven.db.ticket.models import TicketDBO, TicketProductDBO
from driven.db.user.models import UserDBO


class TicketDBRepositoryAdapter(TicketDBRepositoryPort):
    def __init__(self):
        pass

    def save(self, ticket: Ticket):
        products_dbo = []

        # Crear la tienda
        store_dbo = StoreDBO.objects.create(
            location_info=ticket.location
        )

        user_dbo, created = UserDBO.objects.get_or_create(
            email=ticket.email
        )

        # Crear el ticket
        ticket_dbo = TicketDBO.objects.create(
            date_raw=ticket.date,
            location=store_dbo,
            email=user_dbo,
            total=ticket.total
        )

        for product in ticket.products:
            product_dbo, created = ProductDBO.objects.get_or_create(
                name=product.name
            )

            product_history_price = ProductPriceHistoryDBO.objects.create(
                product=product_dbo,
                date_raw=ticket.date,
                price=product.price,
                price_per_unit=product.price_per_unit
            )

            TicketProductDBO.objects.create(
                ticket=ticket_dbo,
                product=product_dbo,
                quantity=product.quantity,
                history_price=product_history_price,
                units=product.price_per_unit
            )

            # Añadir product_dbo a la lista en lugar de ticket_product_dbo
            products_dbo.append(product_dbo)

        # Asignar la lista de productos (ProductDBO) a la relación ManyToMany
        ticket_dbo.products.set(products_dbo)

