from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.post import PostCreate, PostOut, PostPartialUpdate , PostImg
from crud.post import create_post, get_all_posts, get_post, update_post, delete_post ,create_img, get_all_imgs, get_img_by_id, delete_img

router = APIRouter()

@router.post("/post", response_model=PostOut)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)

@router.get("/getpost", response_model=list[PostOut])
def read_posts(db: Session = Depends(get_db)):
    return get_all_posts(db)

@router.get("/post/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.patch("/post/{post_id}", response_model=PostOut)
def patch_post(post_id: int, post: PostPartialUpdate, db: Session = Depends(get_db)):
    updated = update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated

@router.delete("/post/{post_id}")
def remove_post(post_id: int, db: Session = Depends(get_db)):
    deleted = delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}




@router.post("/img", response_model=PostImg)
def create_image(img_data: PostImg, db: Session = Depends(get_db)):
    return create_img(db, img_data)

@router.get("/getimg", response_model=list[PostImg])
def list_images(db: Session = Depends(get_db)):
    return get_all_imgs(db)

@router.get("/img/{img_id}", response_model=PostImg)
def get_image(img_id: int, db: Session = Depends(get_db)):
    img = get_img_by_id(db, img_id)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    return img

@router.delete("/img/{img_id}")
def remove_image(img_id: int, db: Session = Depends(get_db)):
    deleted = delete_img(db, img_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Image not found")
    return {"message": "Image deleted successfully"}
