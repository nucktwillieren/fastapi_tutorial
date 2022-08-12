from fastapi import APIRouter, status, HTTPException, Response
from .database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from . import schema
from . import models

Base.metadata.create_all(engine)

router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[schema.PostOutput], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db)):

    post = db.query(models.Post).all()

    return post


@router.get("/{id}", response_model=schema.PostOutput, status_code=status.HTTP_200_OK)
def get_detail(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post


@router.post("", status_code=status.HTTP_201_CREATED)
def create_one(post: schema.PostInput, db: Session = Depends(get_db)):

    post = models.Post(**post.dict())

    db.add(post)
    db.commit()
    db.refresh(post)

    return {"data": post}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_one(id: int, post: schema.PostInput, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post_query.update(post.dict(), synchronize_session=False)

    db.commit()

    return {"data": post}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one(id: int, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if not post_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
