from typing import Optional

import strawberry


@strawberry.input
class AddTaskInput:
    title: str
    description: Optional[str] = None
    board_id: str


@strawberry.input
class UpdateTaskInput:
    id: strawberry.ID
    status: str


@strawberry.input
class AddBoardInput:
    title: str
    description: Optional[str] = None


@strawberry.input
class UpdateBoardInput:
    id: strawberry.ID
    status: str
