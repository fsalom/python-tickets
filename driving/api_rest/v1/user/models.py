from pydantic import BaseModel


class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True