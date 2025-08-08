from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.post import PostCreate, PostOut , PostPartialUpdate
from crud import post as crud_post

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=PostOut)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud_post.create_post(db, post)

@router.get("/", response_model=list[PostOut])
def read_posts(db: Session = Depends(get_db)):
    return crud_post.get_all_posts(db)

@router.get("/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud_post.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.patch("/{post_id}", response_model=PostOut)
def update_post(post_id: int, post: PostPartialUpdate, db: Session = Depends(get_db)):
    updated = crud_post.update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted = crud_post.delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
