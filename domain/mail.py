from domain.ticket import Ticket


class Mail:
    def __init__(self, email: str, subject: str, content: str, date_raw: str):
        self.email = email
        self.date_raw = date_raw
        self.subject = subject
        self.content = content
