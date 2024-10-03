from typing import Annotated
from asgiref.sync import sync_to_async
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from application.services.authentication_services import AuthenticationServices
from infrastructure.di.authentication.injector import AuthenticationInjector

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user_or_refuse(token: Annotated[str, Depends(oauth2_scheme)],
                             authentication_service: AuthenticationServices
                             = Depends(AuthenticationInjector().get_service)):
    user = await sync_to_async(authentication_service.get_user)(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    return user
