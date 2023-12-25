import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from resolvers import (
    add_task,
    delete_task,
    get_task,
    get_tasks,
    update_task,
    add_board,
    delete_board,
    get_board,
    get_boards,
    update_board,
)
import asyncio


from web.task.types import TaskType, BoardType
from contexts import get_context
from typing import List


@strawberry.type
class Query:
    task: TaskType = strawberry.field(resolver=get_task)
    tasks: list[TaskType] = strawberry.field(resolver=get_tasks)
    board: BoardType = strawberry.field(resolver=get_board)
    boards: list[BoardType] = strawberry.field(resolver=get_boards)


@strawberry.type
class Mutation:
    task_add: TaskType = strawberry.field(resolver=add_task)
    task_update: TaskType = strawberry.field(resolver=update_task)
    task_delete: TaskType = strawberry.field(resolver=delete_task)
    board_add: BoardType = strawberry.field(resolver=add_board)
    board_update: BoardType = strawberry.field(resolver=update_board)
    board_delete: BoardType = strawberry.field(resolver=delete_board)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def tasks_in_board(self, board_id: str, info: Info) -> List[TaskType]:
        while True:
            board = get_board(board_id, info)
            yield board.tasks
            await asyncio.sleep(1.5)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription)
task_app = GraphQLRouter(schema, context_getter=get_context)
