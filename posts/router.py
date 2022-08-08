from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/posts")


@router.get("/")
def get_all():
    pass
