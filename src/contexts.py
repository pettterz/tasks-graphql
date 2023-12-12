from fastapi import Depends
from strawberry.fastapi import BaseContext

from database import get_db
from domain.service.task_service import TaskService
from infra.repository.task_repository import TaskRepository
from domain.service.board_service import BoardService
from infra.repository.board_repository import BoardRepository


def init_task_repository(db=Depends(get_db)):
    return TaskRepository(db)


def init_task_service(task_repository: TaskRepository =
                      Depends(init_task_repository)):
    return TaskService(
        task_repository
    )


class TaskContext(BaseContext):
    def __init__(self, task: TaskService):
        self.__task: TaskService = task

    def get_task(self):
        return self.__task


class MergedContext(BaseContext):
    def __init__(self, task: TaskService, board: BoardService):
        self.__task: TaskService = task
        self.__board: BoardService = board

    def get_task(self):
        return self.__task

    def get_board(self):
        return self.__board


class TaskServicesContext(BaseContext):
    def __init__(self, task: TaskService):
        self.__task: TaskService = task

    def get_task(self):
        return self.__task


def init_board_repository(db=Depends(get_db)):
    return BoardRepository(db)


def init_board_service(board_repository: BoardRepository =
                       Depends(init_board_repository)):
    return BoardService(
        board_repository
    )


# class BoardContext(BaseContext):
#     def __init__(self, board: BoardService):
#         self.__board: BoardService = board

#     def get_board(self):
#         return self.__board


# class BoardServicesContext(BaseContext):
#     def __init__(self, board: BoardService):
#         self.__board: BoardService = board

#     def get_board(self):
#         return self.__board


# async def get_task_context(
#         task_service: TaskService = Depends(init_task_service)
# ) -> TaskContext:
#     return TaskContext(
#         task=task_service
#     )


# async def get_board_context(
#         board_service: BoardService = Depends(init_board_service)
# ) -> BoardContext:
#     return BoardService(
#         board=board_service
#     )


async def get_context(
        task_service: TaskService = Depends(init_task_service),
        board_service: BoardService = Depends(init_board_service)
) -> MergedContext:
    return MergedContext(
        task=task_service,
        board=board_service
    )
