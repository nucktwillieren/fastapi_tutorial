from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

template = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def index_page(request: Request):
    context = {"request": request, "ids": [1, 2, 3, 4]}

    return template.TemplateResponse("index.html", context=context)
