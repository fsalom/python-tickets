from domain.product import Product


class Ticket:
    def __init__(self, id_ticket: str,
                 products: [Product],
                 total: float,
                 iva: float,
                 date: str,
                 email: str,
                 location: str):
        self.id = id_ticket
        self.products = products
        self.total = total
        self.date = date
        self.email = email
        self.location = location
        self.iva = iva
