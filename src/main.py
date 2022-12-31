from fastapi import FastAPI

from . import models
from .database import engine
from .routers import user_router, friend_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
app.include_router(user_router.router)
app.include_router(friend_router.router)


@app.get("/")
def root():
    return {"message": "To interact directly with the appy, add /docs to the url"}