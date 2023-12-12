from typing import Optional

import strawberry


@strawberry.input
class AddTaskInput:
    title: str
    description: Optional[str] = None


@strawberry.input
class UpdateTaskInput:
    id: strawberry.ID
    status: str
