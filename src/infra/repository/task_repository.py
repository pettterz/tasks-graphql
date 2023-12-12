from sqlalchemy.orm import Session

from infra.repository.models import Task


class TaskRepository:
    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(self, id_: str) -> Task:
        task = self.__db.query(Task).get(id_)

        return task

    def find_all(self) -> list[Task]:
        # tasks = list(cls._store.values())
        tasks = self.__db.query(Task).all()

        return tasks

    def save(self, task: Task) -> None:
        self.__db.add(task)
        self.__db.commit()

    def delete(self, task: Task) -> None:
        self.__db.delete(task)
        self.__db.commit()
