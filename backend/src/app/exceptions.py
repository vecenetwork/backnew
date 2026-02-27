from fastapi import HTTPException, status


class ApiException(Exception):
    status_code: int
    detail: str

    def __init__(self, msg: str):
        self.detail = msg
        super().__init__(msg)

    def raise_http_exception(self):
        raise HTTPException(status_code=self.status_code, detail=self.detail)


class Missing(ApiException):
    status_code = status.HTTP_404_NOT_FOUND


class Duplicate(ApiException):
    status_code = status.HTTP_409_CONFLICT


class InvalidToken(ApiException):
    status_code = status.HTTP_401_UNAUTHORIZED


class WrongPassword(ApiException):
    status_code = status.HTTP_401_UNAUTHORIZED


class Unauthorized(ApiException):
    status_code = status.HTTP_401_UNAUTHORIZED


class ConfigurationError(ApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class PermissionDenied(ApiException):
    status_code = status.HTTP_403_FORBIDDEN


class InvalidFavoriteOperation(ApiException):
    """Raised when trying to favorite an already favorite subscription or unfavorite a non-favorite one."""
    def __init__(self, is_favorite: bool):
        action = "add to favorites" if is_favorite else "remove from favorites"
        state = "already favorite" if is_favorite else "not favorite"
        super().__init__(f"Cannot {action} subscription that is {state}")
        self.status_code = 400


class MaxFavoritesReached(ApiException):
    """Raised when trying to add more favorites than allowed."""
    def __init__(self, max_favorites: int):
        super().__init__(f"Cannot add more favorites. Maximum allowed is {max_favorites}")
        self.status_code = 400
