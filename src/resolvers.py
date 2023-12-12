import strawberry

from web.task.inputs import AddTaskInput, UpdateTaskInput
from web.task.types import TaskType, BoardType
from strawberry.types import Info


def get_task(id: strawberry.ID, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.find(id)

    return task


def get_tasks(info: Info) -> list[TaskType]:
    service = info.context.get_task()
    tasks = service.find_all()

    return tasks


def add_task(task_input: AddTaskInput, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.create(**task_input.__dict__)

    return task


def update_task(task_input: UpdateTaskInput, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.update(**task_input.__dict__)

    return task


def delete_task(id: strawberry.ID, info: Info) -> TaskType:
    service = info.context.get_task()
    task = service.delete(id)

    return task


def get_board(id: strawberry.ID, info: Info) -> BoardType:
    service = info.context.get_board()
    board = service.find(id)

    return board


def get_boards(info: Info) -> list[BoardType]:
    service = info.context.get_board()
    boards = service.find_all()

    return boards


def add_board(board_input: AddTaskInput, info: Info) -> BoardType:
    service = info.context.get_board()
    board = service.create(**board_input.__dict__)

    return board


def update_board(board_input: UpdateTaskInput, info: Info) -> BoardType:
    service = info.context.get_board()
    board = service.update(**board_input.__dict__)

    return board


def delete_board(id: strawberry.ID, info: Info) -> BoardType:
    service = info.context.get_board()
    board = service.delete(id)

    return board