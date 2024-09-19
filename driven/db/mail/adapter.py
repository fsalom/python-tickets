from application.ports.driven.database.mail.db_repository import MailDBRepositoryPort


class MailDBRepositoryAdapter(MailDBRepositoryPort):
    def __init__(self):
        print("")

    def save(self, mail: str):
        pass

