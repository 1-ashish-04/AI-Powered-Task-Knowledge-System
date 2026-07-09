from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base
from app.models.task_document import task_documents

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(Text)

    priority = Column(
        String(20),
        default="Medium"
    )

    status = Column(
        String(20),
        default="Pending"
    )

    deadline = Column(
        DateTime,
        nullable=True
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )

    assigned_user = relationship(
        "User",
        foreign_keys=[assigned_to],
        back_populates="assigned_tasks"
    )

    creator = relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_tasks"
    )

    documents = relationship(
    "Document",
    secondary=task_documents,
    back_populates="tasks"
)