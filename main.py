from fastapi import FastAPI
from data import db_session
from data.__all_models import User
from data import schemas

app = FastAPI()
db_session.global_init('db/blogs.db')

 
@app.post('/api/reg_user', response_model=schemas.User)
def reg_user(new_user: schemas.User):
    new_user = User(**new_user.dict())
    session = db_session.create_session()
    session.add(new_user)
    session.commit()
    return f"Ok!\n{new_user}"


@app.get('/')
def start_page():
    return 'Hello!'