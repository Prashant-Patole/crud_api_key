from fastapi import FastAPI
from database.database import Base, engine
from routers import post

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Content Post API with NeonDB")

app.include_router(post.router)
