from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class User(BaseModel):
    email: EmailStr
    name: str
    surname: str
    age: int
    password: str

    class Config:
        orm_mode = True


class Article(BaseModel):
    author: str
    text: str
    # collaborators: str
    start_date: datetime
    is_commentable: bool


class Comment(BaseModel):
    author: str
    text: str
    post_datetime: datetime
    article_id: int
