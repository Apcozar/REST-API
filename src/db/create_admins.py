from sqlalchemy.orm import Session

from ..models.users import Users
from ..core.security import hash
from ..core.config import settings


ADMIN_PWD = settings.admin_pwd

def create_admins(session: Session):

    admin1 = Users(
        name = "admin",
        surname = "admin1",
        username = "admin1",
        age = 0,
        gender = "",
        email = "admin@admin.com",
        password = hash(ADMIN_PWD),
        is_admin = True
    )

    existing_admin1 = session.query(Users).filter(Users.name == admin1.name).first()

    if not existing_admin1:
        session.add(admin1)
        session.commit()
        session.refresh(admin1)



