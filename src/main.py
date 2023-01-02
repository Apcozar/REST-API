from fastapi import FastAPI

from .models.base import Base
from .db.session import engine
from .routers.base import api_router

def create_tables():
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
def root():
    return {"message": "To interact directly with the API, add /docs to the url"}