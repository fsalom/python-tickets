from domain.ticket import Ticket


class Mail:
    def __init__(self, mail: str, subject: str, content: str):
        self.mail = mail
        self.subject = subject
        self.content = content
