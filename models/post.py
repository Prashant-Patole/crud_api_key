from sqlalchemy import Column, Integer, String
from database.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)


class ImgPost(Base):
    __tablename__ ="imgdata"

    id = Column(Integer , primary_key=True , index=True)
    img =Column(String , nullable=False)
    description =Column(String , nullable=False)