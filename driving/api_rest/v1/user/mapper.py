from domain.user import User
from driving.api_rest.v1.user.models import UserResponse


class UserDTOMapper:

    @staticmethod
    def to_dto(user: User) -> UserResponse:
        return UserResponse(username=user.email, email=user.email)
