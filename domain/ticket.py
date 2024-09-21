from domain.product import Product


class Ticket:
    def __init__(self, products: [Product], total: float, date: str, email: str, location: str):
        self.products = products
        self.total = total
        self.date = date
        self.email = email
        self.location = location
