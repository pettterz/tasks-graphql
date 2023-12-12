import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from task import Task


@dataclass
class Board:
    title: str
    description: Optional[str] = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    tasks: list[Task] = list()
