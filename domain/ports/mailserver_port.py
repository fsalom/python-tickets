from abc import ABC, abstractmethod


class MailServerPort(ABC):
    @abstractmethod
    async def handle_DATA(self, server, session, envelope):
        pass
