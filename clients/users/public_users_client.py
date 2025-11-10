from httpx import Response
from clients.APIClient import APIClient
from typing import TypedDict


class CreateUserRequest(TypedDict):
    """
    Структура данных для создания пользователя через API

    Attributes:
        username (str): уникальное имя пользователя
        email (str): электронная почта пользователя
        password (str): пароль пользователя
    """
    username: str
    email: str
    password: str


class PublicUsersClient(APIClient):
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Создание нового пользователя через POST /api/v1/users.

        Args:
            request (CreateUserRequest): Данные пользователя для создания.
                Содержит username, email и password.

        Returns:
            Response: Объект httpx.Response, содержащий ответ сервера.
        """
        response = self.post("/api/v1/users", json=request)
        return response
