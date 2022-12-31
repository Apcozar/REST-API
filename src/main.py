from fastapi import FastAPI
from . import models
from .database import engine
from .routers import friend_repository, user_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
app.include_router(user_router.router)
app.include_router(friend_repository.router)


@app.get("/")
def root():
    return {"message": "To interact directly with the appy, add /docs to the url"}