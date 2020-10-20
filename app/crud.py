from sqlalchemy.orm import Session
from app.models import *
from app.schemas import *

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name, img=author.img, link=author.link)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_author_by_name(db: Session, author_name: str):
    return db.query(Author).filter(Author.name == author_name).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(os_type=user.os_type, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()
