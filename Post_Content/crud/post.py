from sqlalchemy.orm import Session
from models.post import Post
from schemas.post import PostCreate , PostPartialUpdate

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_all_posts(db: Session):
    return db.query(Post).all()

def update_post(db: Session, post_id: int, updated_data: PostPartialUpdate):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None

    # Update only the fields that are provided
    if updated_data.title is not None:
        post.title = updated_data.title
    if updated_data.body is not None:
        post.body = updated_data.body

    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
