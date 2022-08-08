import fastapi
from pydantic import BaseModel
from posts.router import router as post_router

app = fastapi.FastAPI()

app.include_router(post_router)
