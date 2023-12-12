from typing import List

from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    registry,
    relationship,
    mapped_column,
    Mapped
)
from sqlalchemy.sql import func
import uuid


class Status(str, Enum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'


reg = registry()


@reg.mapped_as_dataclass
class Task:
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(default="")
    description: Mapped[str] = mapped_column(default="")
    status: Mapped[str] = mapped_column(default="todo")
    updated_at: Mapped[datetime] = mapped_column(default=func.now())
    board_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("boards.id"),
                                                default=uuid.uuid4)
    board: Mapped["Board"] = relationship(default=None)


@reg.mapped_as_dataclass
class Board:
    __tablename__ = "boards"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(default="")
    description: Mapped[str] = mapped_column(default="")
    updated_at: Mapped[datetime] = mapped_column(default=func.now())

    tasks: Mapped[List["Task"]] = relationship(
        default_factory=list, back_populates="board"
    )
    # tasks: list["Task"] = relationship(
    #     "Task", back_populates="board"
    # )

    # __annotations__ = {"tasks": "Mapped[Task]"}



    # __annotations__ = {"board": "Mapped[Board]"}
    # __mapper_args__ = {  # type: ignore
    #     "properties": {
    #         "board": relationship("Board", back_populates="tasks"),
    #     }
    # }


# # Taskテーブルの定義
# task = Table(
#     'task',
#     mapper_registry.metadata,
#     Column('id', UUIDType(binary=False), primary_key=True, default=uuid.uuid4),
#     Column('description', String(200)),
#     Column('title', String(200)),
#     Column('status', Enum(Status)),
#     Column('updated_at', DateTime, default=func.now()),
#     Column('board_id', ForeignKey('board.id'))
# )
# mapper_registry.map_imperatively(Task, task)

# Define for Board



# board = Table(
#     'board',
#     mapper_registry.metadata,
#     Column('id', UUIDType(binary=False), primary_key=True, default=uuid.uuid4),
#     Column('description', String(200)),
#     Column('title', String(200)),
#     Column('updated_at', DateTime, default=func.now())
# )
# mapper_registry.map_imperatively(Board, board)
