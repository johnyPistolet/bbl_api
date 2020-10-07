from sqlalchemy.orm import Session
import models, schemas

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name, img=author.img, link=author.link)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_author_by_name(db: Session, author_name: str):
    return db.query(models.Author).filter(models.Author.name == author_name).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(os_type=user.os_type, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()