#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from application.services.mail_processor_services import MailProcessorServices
from driven.db.mail.adapter import MailDBRepositoryAdapter
from driven.db.ticket.adapter import TicketDBRepositoryAdapter
from driven.mail.mail_repository_adapter import MailRepositoryAdapter
from driving.mails.adapter import MailsAdapter


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    mail_repository_adapter = MailRepositoryAdapter()
    mail_db_repository_adapter = MailDBRepositoryAdapter()
    ticket_db_repository_adapter = TicketDBRepositoryAdapter()
    service = MailProcessorServices(mail_repository=mail_repository_adapter,
                                    mail_db_repository=mail_db_repository_adapter,
                                    ticket_db_repository=ticket_db_repository_adapter)
    adapter = MailsAdapter(service=service)
    print("ADAPTER")
    adapter.read(1)
