from pydantic import BaseModel


class AuthenticationResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str
    scope: str


class AuthenticationRequest(BaseModel):
    username: str
    password: str
    client_id: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "",
                    "password": "",
                    "client_id": ""
                }
            ]
        }
    }


class AuthenticationRefreshRequest(BaseModel):
    refresh_token: str
    client_id: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "refresh_token": "",
                    "client_id": ""
                }
            ]
        }
    }
