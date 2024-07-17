import asyncio

from aiosmtpd.controller import Controller

from infrastructure.adapter.mailserver.mailserver_adapter import MailServer


if __name__ == "__main__":
    handler = MailServer()
    controller = Controller(handler, hostname='localhost', port=1025)
    controller.start()
    print("Servidor SMTP corriendo en localhost:1025")

    try:
        asyncio.run(asyncio.sleep(9999999))
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()
