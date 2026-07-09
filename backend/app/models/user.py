from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="users")

    uploaded_documents = relationship(
        "Document",
        back_populates="uploader"
    )

    assigned_tasks = relationship(
        "Task",
        foreign_keys="Task.assigned_to",
        back_populates="assigned_user"
    )

    created_tasks = relationship(
        "Task",
        foreign_keys="Task.created_by",
        back_populates="creator"
    )

    activities = relationship(
        "ActivityLog",
        back_populates="user"
    )