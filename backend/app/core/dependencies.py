from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db


def get_database(
    db: Session = Depends(get_db)
):
    return db