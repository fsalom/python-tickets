from fastapi import FastAPI

from infrastructure.di.authentication.container import AuthenticationContainer
from infrastructure.di.tickets.container import TicketContainer


def add_containers(app: FastAPI):
    authentication_container = AuthenticationContainer()
    tickets_container = TicketContainer()
    app.authentication_container = authentication_container
    app.tickets_container = tickets_container
