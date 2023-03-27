from typing import Optional

from project.dao.director import DirectorsDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: DirectorsDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """
        Сервис получения одного режиссера
        """
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """
        Сервис получения всех режиссеров
        """
        return self.dao.get_all(page=page)
