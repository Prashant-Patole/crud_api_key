from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database.database import Base, engine
from routers import post
import time

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Content Post API with NeonDB")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} completed in {process_time:.4f}s with status {response.status_code}")
    
    return response

app.include_router(post.router)
