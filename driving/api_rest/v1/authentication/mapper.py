from domain.tokens import Tokens
from driving.api_rest.v1.authentication.models import AuthenticationResponse


class AuthenticationDTOMapper:

    @staticmethod
    def to_dto(tokens: Tokens) -> AuthenticationResponse:
        return AuthenticationResponse(access_token=tokens.access_token,
                                      refresh_token=tokens.refresh_token,
                                      expires_in=tokens.expires_in,
                                      token_type=tokens.token_type,
                                      scope=tokens.scope)
