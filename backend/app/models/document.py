from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base
from app.models.task_document import task_documents

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    filename = Column(String(255), nullable=False)

    filepath = Column(String(500), nullable=False)

    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    uploader = relationship(
        "User",
        back_populates="uploaded_documents"
    )

    tasks = relationship(
    "Task",
    secondary=task_documents,
    back_populates="documents"
)