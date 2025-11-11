from typing import TypedDict

from clients.APIClient import APIClient
from httpx import Response

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class UpdateExerciseRequestDict(TypedDict):
    """
       Описание структуры запроса
       """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class CreateExerciseRequestDict(TypedDict):
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


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения запроса
        :param query: Словарь с courseId
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_view(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)



    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод для отправки запроса
        :param request: Словарь с update_exercises
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления
        :param exercise_id индификатор
        :return: Ответ от сервера в виду объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")