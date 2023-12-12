from datetime import datetime
from typing import Optional

from infra.repository.models import Board
from infra.repository.board_repository import BoardRepository


class BoardService:
    def __init__(self, repo: BoardRepository) -> None:
        self.__repo = repo

    @property
    def repo(self) -> type[BoardRepository]:
        return self.__repo

    def find(self, id: str) -> Board:
        board = self.repo.find_by_id(id)

        return board

    def find_all(self) -> list[Board]:
        boards = self.repo.find_all()

        return boards

    def create(self, *, title: str, description: Optional[str] = None) -> Board:
        board = Board(title=title, description=description)
        self.repo.save(board)

        return board

    def update(self, *, id: str, description: str) -> Board:
        board = self.repo.find_by_id(id)
        board.description = description
        board.updated_at = datetime.utcnow()
        self.repo.save(board)

        return board

    def delete(self, id: str) -> Board:
        board = self.repo.find_by_id(id)
        self.repo.delete(board)

        return board
