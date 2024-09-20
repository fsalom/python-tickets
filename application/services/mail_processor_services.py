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

    def process(self):
        mails = self.mail_repository.read()
        for mail in mails:
            ticket = self.analyze(content=mail.content, email=mail.mail)
            self.ticket_db_repository.save(ticket)

    def analyze(self, content: str, email: str) -> Ticket:
        receipt_text = content
        # 1. Extraer la ubicación
        location_pattern = r"(MERCADONA, S.A. A-\d+)(.*?TELÉFONO: \d+)"
        location_match = re.search(location_pattern, receipt_text, re.DOTALL)
        location_info = location_match.group(0) if location_match else "Ubicación no encontrada"

        # 2. Extraer los productos y precios
        products_pattern = r"(\d+) ([A-ZÁÉÍÓÚÑ\+\-\s]+?)\s+(\d+,\d{2})(?:\s+(\d+,\d{2}))?"
        products = re.findall(products_pattern, receipt_text)

        # 3. Extraer los totales
        totals_pattern = r"TOTAL \(€\) (\d+,\d{2})"
        totals_match = re.search(totals_pattern, receipt_text)
        total = totals_match.group(1) if totals_match else "Total no encontrado"

        # 4. Extraer el IVA
        iva_pattern = r"IVA BASE IMPONIBLE \(€\) CUOTA \(€\)(.*?)TOTAL (\d+,\d{2}) (\d+,\d{2})"
        iva_match = re.search(iva_pattern, receipt_text, re.DOTALL)
        iva_info = iva_match.group(1) if iva_match else "Información de IVA no encontrada"
        products_to_save = []
        for product in products:
            quantity, name, price_per_unit, price = product
            if price:
                new_product = Product(name=name, quantity=quantity, price_per_unit=0, price=price_per_unit)
            else:
                new_product = Product(name=name, quantity=quantity, price_per_unit=price_per_unit, price=price)
            products_to_save.append(new_product)

        return Ticket(products=products_to_save, total=total, date="", email=email, location=location_info)
