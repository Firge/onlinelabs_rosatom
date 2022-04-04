from fastapi import FastAPI
from data import db_session
from data.__all_models import User, Comment, Article
from data import schemas

app = FastAPI()
db_session.global_init('db/blogs.db')


@app.get('/api/get_user/{user_id}', response_model=schemas.User)
async def get_user(user_id: int):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    return user


@app.get('/api/get_user_comments/{author_id}', response_model=schemas.Comment)
async def get_user_comments(author_id: int):
    session = db_session.create_session()
    comments = session.query(Comment).filter_by(author=author_id).all()
    return comments


@app.get('/api/get_user_articles/{author_id}', response_model=schemas.Article)
async def get_user_articles(author_id: int):
    session = db_session.create_session()
    articles = session.query(Article).filter_by(author=author_id).all()
    return articles


@app.get('/api/get_article/{article_id}', response_model=schemas.Article)
async def get_article(article_id: int):
    session = db_session.create_session()
    article = session.query(Article).get(article_id)
    return article


@app.get('/api/get_comment/{comment_id}', response_model=schemas.Comment)
async def get_comment(comment_id: int):
    session = db_session.create_session()
    article = session.query(Comment).get(comment_id)
    return article


@app.delete('/api/delete_user/{user_id}')
async def delete_user(user_id: int):
    session = db_session.create_session()
    session.query(User).filter_by(id=user_id).delete()
    return 'Ok'


@app.delete('/api/delete_comment/{comment_id}')
async def delete_comment(comment_id: int):
    session = db_session.create_session()
    session.query(Comment).filter_by(id=comment_id).delete()
    return 'Ok'


@app.delete('/api/delete_article/{article_id}')
async def delete_article(article_id: int):
    session = db_session.create_session()
    session.query(Article).filter_by(id=article_id).delete()
    return 'Ok'


@app.post('/api/change_comment/{comment_id}', response_model=schemas.Comment)
async def change_comment(comment_id: int, new_comment: schemas.Comment):
    session = db_session.create_session()
    session.query(Comment).get(comment_id).update(new_comment)
    session.commit()
    return session.query(Comment).get(comment_id)


@app.post('/api/change_user/{user_id}', response_model=schemas.User)
async def change_comment(user_id: int, new_user: schemas.User):
    session = db_session.create_session()
    session.query(User).get(user_id).update(new_user)
    session.commit()
    return session.query(User).get(user_id)


@app.post('/api/reg_user', response_model=schemas.User)
async def reg_user(new_user: schemas.User):
    print(new_user)
    new_user = User(**new_user.dict())
    session = db_session.create_session()
    session.add(new_user)
    session.commit()
    user = session.query(User).filter(User.id == 1).scalar()
    return user


@app.post('/api/add_comment', response_model=schemas.Comment)
async def add_comment(new_comment: schemas.Comment):
    new_comment = Comment(**new_comment.dict())
    session = db_session.create_session()
    session.add(new_comment)
    session.commit()
    comment = session.query(Comment).filter(Comment.id == 1).scalar()
    return comment


@app.post('/api/add_article', response_model=schemas.Article)
async def add_article(new_article: schemas.Article):
    new_article = Article(**new_article.dict())
    session = db_session.create_session()
    session.add(new_article)
    session.commit()
    article = session.query(Article).filter(Article.id == 1).scalar()
    return article


@app.get('/')
async def start_page():
    return 'Hello!'
