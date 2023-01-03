from sqlalchemy.orm import Session

from ..models.users import Users


def create_admins(session: Session):

    admin1 = Users(
        name = "admin",
        surname = "admin1",
        username = "jsgdgfsgdfd",
        age = 0,
        gender = "",
        is_admin = True
    )

    session.add(admin1)
    session.commit()
    session.refresh(admin1)



