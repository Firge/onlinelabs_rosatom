import datetime
import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class Article(SqlAlchemyBase):
    __tablename__ = 'articles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    text = sa.Column(sa.Text)
    # collaborators = sa.Column(sa.String)
    start_date = sa.Column(sa.DateTime, default=datetime.datetime.now())
    is_commentable = sa.Column(sa.Boolean, default=True)


class Comment(SqlAlchemyBase):
    __tablename__ = 'comments'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    text = sa.Column(sa.Text)
    post_datetime = sa.Column(sa.DateTime, default=datetime.datetime.now())
    article_id = sa.Column(sa.Integer, sa.ForeignKey("articles.id"))


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    age = sa.Column(sa.Integer)
    email = sa.Column(sa.String, unique=True)
    # hashed_password = sa.Column(sa.String)