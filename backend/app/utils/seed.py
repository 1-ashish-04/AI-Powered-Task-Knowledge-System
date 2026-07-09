from sqlalchemy.orm import Session

from app.models.role import Role


def seed_roles(db: Session):

    if db.query(Role).count() == 0:

        db.add(Role(role_name="Admin"))
        db.add(Role(role_name="User"))

        db.commit()