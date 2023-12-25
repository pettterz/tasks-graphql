from datetime import datetime
from typing import Optional

from infra.repository.models import Status, Task
from infra.repository.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self.__repo = repo

    @property
    def repo(self) -> type[TaskRepository]:
        return self.__repo

    def find(self, id: str) -> Task:
        task = self.repo.find_by_id(id)

        return task

    def find_all(self) -> list[Task]:
        tasks = self.repo.find_all()

        return tasks

    def create(self, *, title: str, description: Optional[str] = None,
               board_id: str) -> Task:

        task = Task(title=title, description=description, board_id=board_id)

        self.repo.save(task)

        return task

    def update(self, *, id: str, status: Status) -> Task:
        task = self.repo.find_by_id(id)
        task.status = status
        task.updated_at = datetime.utcnow()
        self.repo.save(task)

        return task

    def delete(self, id: str) -> Task:
        task = self.repo.find_by_id(id)
        self.repo.delete(task)

        return task
