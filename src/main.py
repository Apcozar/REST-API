from fastapi import FastAPI

from .models.base import Base
from .db.database import engine
from .routers import friendships_router, users_router

def create_tables():
    Base.metadata.create_all(bind=engine)


def set_routers(app):
    app.include_router(users_router.router)
    app.include_router(friendships_router.router)


def start_application():
    app = FastAPI()
    create_tables()
    set_routers(app)
    return app


app = start_application()

@app.get("/")
def root():
    return {"message": "To interact directly with the API, add /docs to the url"}