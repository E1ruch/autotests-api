from typing import TypedDict

from clients.APIClient import APIClient
from httpx import Response, Request

class getView(TypedDict):
    """
    Описание структуры запроса
    """
    courseId: str

class update_exercises(TypedDict):
    """
       Описание структуры запроса
       """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class create_exercises(TypedDict):
    """
       Описание структуры запроса
       """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str

class get_exercises(TypedDict):
    """
       Описание структуры запроса
       """
    exercise_id: str

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: getView) -> Response:
        """
        Метод для получения запроса
        :param query: Словарь с courseId
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def post_create_exercise_api(self, create_exercises) -> Response:
        """
        Метод для отправки запроса
        :param request: Словарь с create_exercises
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=create_exercises)

    def get_exercise_view(self, exercise_id: str) -> Response:
        """
        Метод для информации о конкретном
        :param exercise_id индификатор
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: update_exercises) -> Response:
        """
        Метод для отправки запроса
        :param request: Словарь с update_exercises
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str, request) -> Response:
        """
        Метод для удаления
        :param exercise_id индификатор
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}", json=request)