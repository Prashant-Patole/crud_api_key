from sqlalchemy.orm import Session
from models.post import Post, ImgPost
from schemas.post import PostCreate, PostPartialUpdate, PostImg

# -------------------- POSTS CRUD --------------------
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

# -------------------- IMAGES CRUD --------------------
def create_img(db: Session, img_data: PostImg):
    new_img = ImgPost(
        img=img_data.img,
        description=img_data.description
    )
    db.add(new_img)
    db.commit()
    db.refresh(new_img)
    return new_img

def get_all_imgs(db: Session):
    return db.query(ImgPost).all()

def get_img_by_id(db: Session, img_id: int):
    return db.query(ImgPost).filter(ImgPost.id == img_id).first()

def delete_img(db: Session, img_id: int):
    img_record = db.query(ImgPost).filter(ImgPost.id == img_id).first()
    if img_record:
        db.delete(img_record)
        db.commit()
    return img_record
