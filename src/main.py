from fastapi import FastAPI, HTTPException, Response, status, Depends
from . import models, schemas
from .database import engine, get_db
from .routers import user, friendship

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
app.include_router(user.router)
app.include_router(friendship.router)


@app.get("/")
def root():
    return {"message": "To interact directly with the appy, add /docs to the url"}