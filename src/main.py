from fastapi import FastAPI

from . import models
from .database import engine
from .routers import friendships_router, users_router

app = FastAPI()
    
app.include_router(users_router.router)
app.include_router(friendships_router.router)


@app.get("/")
def root():
    return {"message": "To interact directly with the API, add /docs to the url"}