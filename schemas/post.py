from typing import Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    body: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int

    class Config:
        orm_mode = True

class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class PostImg(BaseModel):
    img:str
    description:str

    class Config:
        orm_mode = True
        