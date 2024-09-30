from datetime import timedelta

from django.contrib.auth import authenticate
from django.utils import timezone
from oauth2_provider.models import RefreshToken, Application, AccessToken
from oauth2_provider.settings import oauth2_settings
from application.ports.driven.database.authentication.db_repository import AuthenticationDBRepositoryPort
from domain.tokens import Tokens
from domain.user import User


class AuthenticationDBRepositoryAdapter(AuthenticationDBRepositoryPort):
    def logout(self):
        pass

    def login(self, username: str, password: str, client_id: str) -> Tokens | None:
        user = authenticate(username=username, password=password)
        if user is None:
            return None

        try:
            application = Application.objects.get(client_id=client_id)
        except Application.DoesNotExist:
            return None

        now = timezone.now()
        expires = now + timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)

        access_token = AccessToken.objects.create(
            user=user,
            application=application,
            expires=expires,
            token=oauth2_settings.ACCESS_TOKEN_GENERATOR(),
            scope="read write"
        )

        refresh_token = RefreshToken.objects.create(
            user=user,
            token=oauth2_settings.REFRESH_TOKEN_GENERATOR(),  # Genera el refresh token
            application=application,
            access_token=access_token,
        )

        return Tokens(
            access_token=access_token.token,
            refresh_token=refresh_token.token,
            expires_in=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
            token_type='Bearer',
            scope=access_token.scope
        )

    def get_user(self, token: str) -> User | None:
        try:
            access_token = AccessToken.objects.filter(token=token, expires__gt=timezone.now()).first()
            if access_token is None:
                return None
            user = access_token.user
            return user
        except Exception as e:
            return None
