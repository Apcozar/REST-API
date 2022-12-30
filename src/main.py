from fastapi import FastAPI, HTTPException, Response, status, Depends
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.InUser, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, surname=user.surname, description=user.description)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"data": new_user}

@app.get("/friend", status_code=status.HTTP_201_CREATED)
def create_friendship(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    new_friendship = models.Friendship(user_id=user_id, friend_id=friend_id)
    db.add(new_friendship)
    db.commit()
    db.refresh(new_friendship)
    return {"data": new_friendship}

@app.get("/users", status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return {"data": users}

@app.get("/user/{id}", status_code=status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    return {"data": user}

@app.get("/friends/{id}", status_code=status.HTTP_200_OK)
def get_friends(id: int, db: Session = Depends(get_db)):
    friends = db.query(models.Friendship).filter(models.Friendship.user_id== id).all()
    return {"data": friends}

@app.post("/user/{id}")
def update_user(id: int, updated_user: schemas.InUser, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    user_query.update(updated_user.dict(), synchronize_session=False)

    db.commit()

    return {"data": "succesful"}

@app.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)

    user = user_query.first()

    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="user with id: {id} does not exist")

    user_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/friend", status_code=status.HTTP_204_NO_CONTENT)
def delete_friend(user_id: int, friend_id: int, db: Session = Depends(get_db)):
    friendship_query = db.query(models.Friendship).filter(models.Friendship.user_id == user_id and 
        models.Friendship.friend_id == friend_id)

    friendship = friendship_query.first()

    if friendship == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail="This users are not friends")

    friendship_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

    