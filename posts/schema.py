from pydantic import BaseModel
from typing import List, Union


class BasePost(BaseModel):
    title: str
    description: Union[str, None] = None


class PostInput(BasePost):
    pass

class PostOutput(BasePost):
    id: int
    class Config:
        orm_mode = True