from typing import Annotated

from asgiref.sync import sync_to_async
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from application.di.authentication.injector import AuthenticationInjector
from application.ports.driving.authentication_service_port import AuthenticationServicePort
from application.services.authentication_services import AuthenticationServices
from domain.user import User
from driving.api_rest.decorator.authenticated import authenticated, oauth2_scheme

user_router = APIRouter()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                           authentication_service: AuthenticationServices
                           = Depends(AuthenticationInjector().get_authentication_service())):
    user = await sync_to_async(authentication_service.get_user)(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    return user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@user_router.get('/users/me')
async def me(user: Annotated[User, Depends(get_current_user)]):
    return {"username": user.email, "email": user.email}
