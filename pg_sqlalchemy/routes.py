from typing import List
from fastapi import HTTPException, Depends
from fastapi import APIRouter

from sqlalchemy.orm import Session
from starlette import status

import models
import schemas
from db_base import get_db

apirouter = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@apirouter.get('/', response_model=List[schemas.CreatePost])
def test_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return  post

@apirouter.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost])
def test_posts_sent(post_post:schemas.CreatePost, db:Session = Depends(get_db)):

    new_post = models.Post(**post_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]


@apirouter.get('/{id}', response_model=schemas.CreatePost, status_code=status.HTTP_200_OK)
def get_test_one_post(id:int ,db:Session = Depends(get_db)):

    idv_post = db.query(models.Post).filter(models.Post.id == id).first()

    if idv_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_post

@apirouter.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_test_post(id:int, db:Session = Depends(get_db)):

    deleted_post = db.query(models.Post).filter(models.Post.id == id)


    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()



@apirouter.put('/posts/{id}', response_model=schemas.CreatePost)
def update_test_post(update_post:schemas.PostBase, id:int, db:Session = Depends(get_db)):

    updated_post =  db.query(models.Post).filter(models.Post.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()


    return  updated_post.first()