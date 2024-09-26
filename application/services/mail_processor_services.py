import re

from application.ports.driven.database.mail.db_repository import MailDBRepositoryPort
from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort
from application.ports.driven.mail.mail_repository_port import MailRepositoryPort
from application.ports.driving.mail_service_port import MailServicePort
from application.ports.driving.tickets_service_port import TicketServicePort
from domain.mail import Mail
from domain.product import Product
from domain.ticket import Ticket


class MailProcessorServices(MailServicePort):
    def __init__(self,
                 mail_repository: MailRepositoryPort,
                 ticket_db_repository: TicketDBRepositoryPort):
        self.mail_repository = mail_repository
        self.ticket_db_repository = ticket_db_repository

    def test(self):
        content = '''MERCADONA, S.A. A-46103834
C/ MENÉNDEZ Y PELAYO 35
46010 VALENCIA
TELÉFONO: 963613959
16/09/2024 10:37 OP: 3049233
FACTURA SIMPLIFICADA: 2475-014-371662
Descripción P. Unit Importe
1 ARROZ INTEGRAL 1,10
1 MOUSSE PROTEIN CHOCO 1,30
1 BOLSA PLASTICO 0,15
1 ARÁNDANO 225 GR 3,09
1 T POLLO NATURAL 1,95
1 AGUACATE
0,236 kg 5,10 €/kg 1,20
TOTAL (€) 8,79
TARJETA BANCARIA 8,79
IVA BASE IMPONIBLE (€) CUOTA (€)
0% 4,29 0,00
10% 3,95 0,40
21% 0,12 0,03
TOTAL 8,36 0,43
TARJ. BANCARIA: **** **** **** 9018
N.C: 098100902 AUT: 558083
AID: A0000000041010 ARC: 00
MASTERCARD
Importe: 8,79 € MASTERCARD
SE ADMITEN DEVOLUCIONES CON TICKET
        '''
        ticket = self.analyze(content=content, email="mail")


    def process(self):
        mails = self.mail_repository.read()
        for mail in mails:
            ticket = self.analyze(content=mail.content, email=mail.mail)
            self.ticket_db_repository.save(ticket)

    def analyze(self, content: str, email: str):
        # ID TICKET
        id_pattern = r"(FACTURA(?: SIMPLIFICADA)?(?:.*?)(\d{4}-\d{3}-\d{6}))"
        id_ticket = re.search(id_pattern, content)
        id_ticket = id_ticket.group(2) if id_ticket else "Número de factura no encontrado"
        # DATE
        date_pattern = r"(\d{2}/\d{2}/\d{4} \d{2}:\d{2})"
        date = re.search(date_pattern, content)
        date = date.group(1) if date else "Fecha no encontrada"
        # PRODUCTS
        products_text = self.extract_products_section(content)
        products_pattern = r"(\d+\s+[a-zA-Z\s-]+)\n?([\d,.]+\s?kg)?\s?(\d+,\d+ €/kg)?\s?(\d+,\d+)"
        products = re.findall(products_pattern, products_text if products_text else "")
        # LOCATION
        location_pattern = r"(MERCADONA, S.A. A-\d+)(.*?TELÉFONO: \d+)"
        location_match = re.search(location_pattern, content, re.DOTALL)
        location_info = location_match.group(0) if location_match else "Ubicación no encontrada"
        # TOTAL
        totals_pattern = r"TOTAL \(€\) (\d+,\d{2})"
        totals_match = re.search(totals_pattern, content)
        total_ticket = totals_match.group(1) if totals_match else "0,0"

        products_exported = []
        for product in products:
            name = product[0].strip()
            weight = product[1].strip() if product[1] else None
            price_kg = product[2].strip() if product[2] else None
            total = product[3].strip()

            product_dict = {
                'name': name,
                'weight': weight,
                'price_kg': price_kg,
                'total': total
            }
            products_exported.append(product_dict)

        results = {
            'date': date,
            'id_ticket': id_ticket,
            'products': products_exported
        }

        print(f"Localización: {location_info}")
        print(f"Fecha: {results['date']}")
        print(f"Número de factura: {results['id_ticket']}")
        print("Productos:")

        products_to_save = []
        for product in results['products']:
            quantity_name = product["name"].split(maxsplit=1)
            quantity = quantity_name[0]
            name = quantity_name[1] if len(quantity_name) > 1 else ""

            weight = "-"
            if product["weight"]:
                weight = product["weight"]

            price_kg = "-"
            if product['price_kg']:
                price_kg = product['price_kg']

            total = product["total"]

            string_total = total.replace(",", ".")
            float_total = float(string_total)

            print(f"{quantity} {name} {weight} {price_kg} {total}")

            new_product = Product(name=name,
                                  quantity=quantity,
                                  price_per_unit=price_kg,
                                  price=float_total,
                                  weight=weight)

            products_to_save.append(new_product)

        string_number = total_ticket.replace(",", ".")
        float_number = float(string_number)
        print(f"Importe: {float_number}")
        return Ticket(id_ticket=id_ticket,
                      products=products_to_save,
                      total=float_number,
                      date=date,
                      email=email,
                      location=location_info,
                      iva=0.0)

    def extract_products_section(self, ticket_text):
        products_pattern = r"Descripción(.+?)TOTAL \(\€\)"
        match = re.search(products_pattern, ticket_text, re.DOTALL)

        if match:
            products_section = match.group(1).strip()
            return products_section
        else:
            return None