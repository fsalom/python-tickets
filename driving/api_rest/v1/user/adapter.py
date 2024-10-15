from typing import Annotated
from fastapi import APIRouter, Depends
from domain.user import User
from driving.api_rest.security import get_user_or_refuse

user_router = APIRouter()


@user_router.get('/users/me')
async def me(user: Annotated[User, Depends(get_user_or_refuse)]):
    return {"username": user.email, "email": user.email}
