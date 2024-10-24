#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import time
import django

from infrastructure.di.tickets.container import TicketContainer


def cronjob():
    sys.stdout.write("Starting cronjob\n")
    sys.stdout.flush()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrastructure.django.settings')
    django.setup()

    from application.services.mail_services import MailServices
    from driven.mail.mail_repository_adapter import MailRepositoryAdapter
    from driving.mails.adapter import MailsAdapter
    from driven.db.mail.adapter import MailDBRepositoryAdapter

    mail_repository_adapter = MailRepositoryAdapter()
    ticket_db_repository_adapter = TicketContainer.db_repository
    mail_db_repository_adapter = MailDBRepositoryAdapter()

    service = MailServices(mail_repository=mail_repository_adapter,
                           ticket_db_repository=ticket_db_repository_adapter,
                           mail_db_repository=mail_db_repository_adapter)

    adapter = MailsAdapter(service=service)
    adapter.schedule_jobs()

    # Simular ejecución periódica para debug
    while True:
        sys.stdout.write("Cronjob is running...\n")
        sys.stdout.flush()
        time.sleep(10)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrastructure.django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    cron_thread = threading.Thread(target=cronjob)
    cron_thread.daemon = True
    cron_thread.start()
    execute_from_command_line(sys.argv)


def test():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrastructure.django.settings')
    django.setup()
    from application.services.mail_services import MailServices
    from driven.mail.mail_repository_adapter import MailRepositoryAdapter
    from driven.db.mail.adapter import MailDBRepositoryAdapter

    mail_repository_adapter = MailRepositoryAdapter()
    ticket_db_repository_adapter = TicketContainer.db_repository
    mail_db_repository_adapter = MailDBRepositoryAdapter()

    service = MailServices(mail_repository=mail_repository_adapter,
                           ticket_db_repository=ticket_db_repository_adapter,
                           mail_db_repository=mail_db_repository_adapter)
    service.test()


if __name__ == '__main__':
    main()
