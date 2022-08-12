import fastapi
from pydantic import BaseModel
from posts.router import router as post_router
from frontend.router import router as fronend_router
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(fronend_router, prefix="")
app.include_router(post_router, prefix="/api/v1")
