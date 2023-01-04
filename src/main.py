from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .models.base import Base
from .db.session import engine, get_session
from .routers.base import api_router
from .db.create_admins import create_admins


def create_tables():
    #Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def set_routers(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI()
    create_tables()
    set_routers(app)
    return app


app = start_application()

@app.get("/")
def root(session: Session = Depends(get_session)):
    create_admins(session)

    return {"message": "To interact directly with the API, add /docs to the url"}