from sqlalchemy.orm import Session

from ..models.users import Users
from ..core.security import hash


def create_admins(session: Session):

    admin1 = Users(
        name = "admin",
        surname = "admin1",
        username = "jsgdgfsgdfd",
        age = 0,
        gender = "",
        email = "apcozar@gmail.com",
        password = hash("test"),
        is_admin = True
    )

    session.add(admin1)
    session.commit()
    session.refresh(admin1)



