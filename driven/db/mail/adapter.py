from application.ports.driven.database.mail.db_repository import MailDBRepositoryPort
from domain.mail import Mail
from driven.db.mail.models import MailDBO


class MailDBRepositoryAdapter(MailDBRepositoryPort):
    def __init__(self):
        print("")

    def save(self, mail: Mail):
        MailDBO.objects.get_or_create(
            date_raw=mail.date_raw,
            email=mail.email,
            subject=mail.subject,
            content=mail.content)
