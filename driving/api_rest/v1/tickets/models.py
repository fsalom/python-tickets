from typing import List, Optional

from pydantic.v1 import BaseModel


class ProductResponse(BaseModel):
    name: str
    quantity: int
    price_per_unit: float
    price: float
    weight: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class TicketResponse(BaseModel):
    id_ticket: str
    products: List[ProductResponse]
    total: float
    iva: float
    date: str
    email: str
    location: str

    class Config:
        arbitrary_types_allowed = True


class AllTicketsResponse(BaseModel):
    num_tickets: int
    tickets: List[TicketResponse]

    class Config:
        arbitrary_types_allowed = True
