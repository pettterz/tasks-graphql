from typing import List

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from sqlalchemy import (Column, DateTime, Enum as EnumColumn, ForeignKey,
                        String)
from sqlalchemy.orm import declarative_base, registry, relationship, Mapped
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid


class Status(str, Enum):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'


Base = declarative_base()
# mapper_registry = registry()


@dataclass
# @mapper_registry.mapped
class Task(Base):
    __tablename__ = "tasks"
    __allow_unmapped__ = True
    title: str = Column('title', String(200))
    id: uuid.UUID = Column('id', UUIDType(binary=False), primary_key=True,
                           default=uuid.uuid4)
    description: str = Column('description', String(200))
    status: Status = Column('status', EnumColumn(Status))
    updated_at: datetime = Column('updated_at', DateTime, default=func.now())
    board_id: uuid.UUID = Column(UUIDType(binary=False),
                                 ForeignKey("boards.id"))
    # board: "Board" = relationship("Board", back_populates="tasks")


@dataclass
class Board(Base):
    __tablename__ = "boards"
    title: str = Column('title', String(200))
    id: uuid.UUID = Column('id', UUIDType(binary=False), primary_key=True,
                           default=uuid.uuid4)
    description: str = Column('description', String(200))
    updated_at: datetime = Column('updated_at', DateTime, default=func.now())
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
