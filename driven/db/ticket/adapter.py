from application.ports.driven.database.ticket.db_repository import TicketDBRepositoryPort


class TicketDBRepositoryAdapter(TicketDBRepositoryPort):
    def __init__(self):
        print("")

    def save(self, mail: str):
        pass

