from datetime import datetime
from typing import Optional, List

import strawberry

from infra.repository.models import Status

StatusType = strawberry.enum(Status, name="Status")


@strawberry.type(name="Task")
class TaskType:
    id: strawberry.ID
    title: str
    description: Optional[str]
    status: StatusType
    updated_at: datetime
    board: "BoardType"
    board_id: str


@strawberry.type(name="Board")
class BoardType:
    id: strawberry.ID
    title: str
    description: Optional[str]
    updated_at: datetime
    tasks: List[TaskType]
