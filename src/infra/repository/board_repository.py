from sqlalchemy.orm import Session
from infra.repository.models import Board


class BoardRepository:
    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(self, id_: str) -> Board:
        board = self.__db.query(Board).get(id_)

        return board

    def find_all(self) -> list[Board]:
        boards = self.__db.query(Board).all()

        return boards

    def save(self, board: Board) -> None:
        self.__db.add(board)
        self.__db.commit()

    def delete(self, board: Board) -> None:
        self.__db.delete(board)
        self.__db.commit()
