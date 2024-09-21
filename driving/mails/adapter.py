from application.ports.driving.mail_service_port import MailServicePort
from apscheduler.schedulers.blocking import BlockingScheduler


class MailsAdapter:
    def __init__(self, service: MailServicePort):
        self.service = service

    def schedule_jobs(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.service.process, 'interval', minutes=1)
        scheduler.start()
