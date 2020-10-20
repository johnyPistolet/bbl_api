from typing import List
from fastapi import FastAPI, Depends, HTTPException
import models
import crud
import schemas
import database
from database import engine
from database import SessionLocal

#from fastapi_admin.factory import app as admin_app
#from fastapi_admin.site import Site

from tortoise.contrib.fastapi import register_tortoise
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#register_tortoise(
#    app,
#    config={
#        'connections': {
#            'default': 'mysql://root:our_sec_pass@localhost:3306/bbl_rest_api',
#        },
#        'apps': {
#        #    'models': {
#        #        'models': ['fastapi_admin.models', 'models'],
#        #        'default_connection': 'default',
#        #    }
#        }
#    }, generate_schemas=True, add_exception_handlers=True,
#)

#register_tortoise(fast_app, config=TORTOISE_ORM, generate_schemas=True)

#app.mount('/admin', admin_app)
#
#@app.on_event('startup')
#async def startup():
#    admin_app.init(
#        admin_secret="test",
#        permission=True,
#        site=Site(
#            name="FastAPI-Admin DEMO",
#            login_footer="FASTAPI ADMIN - FastAPI Admin Dashboard",
#            login_description="FastAPI Admin Dashboard",
#            locale="en-US",
#            locale_switcher=True,
#            theme_switcher=True,
#        ),
#    )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hey! This is BBL API) Nice to meet you here"}

@app.post("/users/", response_model=schemas.User)
async def register_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, new_user.email)
    if(db_user):
        raise HTTPException(status_code=400, detail="User with this email already exist!")
    return crud.create_user(db, new_user)

@app.post("/authors/", response_model=schemas.Author)
async def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.get_author_by_name(db, author_name=author.name)
    if(db_author):
        raise HTTPException(status_code=400, detail="Author already exist!")
    return crud.create_author(db=db, author=author)

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors

@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

