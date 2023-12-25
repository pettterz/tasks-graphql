from typing import List

from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    registry,
    relationship,
    mapped_column,
    Mapped
)
from sqlalchemy.sql import func
import uuid


class Status(str, Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


reg = registry()


def id_factory():
    return str(uuid.uuid4())


@reg.mapped_as_dataclass
class Task:
    __tablename__ = "tasks"

    id: Mapped[str] = mapped_column(String, primary_key=True,
                                    default_factory=id_factory)
    title: Mapped[str] = mapped_column(default="")
    description: Mapped[str] = mapped_column(default="")
    status: Mapped[str] = mapped_column(default="TODO")
    updated_at: Mapped[datetime] = mapped_column(default=func.now())
    board_id: Mapped[str] = mapped_column(String, ForeignKey("boards.id"),
                                          default_factory=uuid.uuid4)
    board: Mapped["Board"] = relationship(default=None)


@reg.mapped_as_dataclass
class Board:
    __tablename__ = "boards"

    id: Mapped[str] = mapped_column(String, primary_key=True,
                                    default_factory=id_factory)
    title: Mapped[str] = mapped_column(default="")
    description: Mapped[str] = mapped_column(default="")
    updated_at: Mapped[datetime] = mapped_column(default=func.now())

    tasks: Mapped[List["Task"]] = relationship(
        default_factory=list, back_populates="board"
    )
