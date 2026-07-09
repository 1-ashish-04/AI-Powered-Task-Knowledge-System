from sqlalchemy import Table, Column, Integer, ForeignKey

from app.database import Base

task_documents = Table(
    "task_documents",
    Base.metadata,

    Column(
        "task_id",
        Integer,
        ForeignKey("tasks.id"),
        primary_key=True
    ),

    Column(
        "document_id",
        Integer,
        ForeignKey("documents.id"),
        primary_key=True
    )
)