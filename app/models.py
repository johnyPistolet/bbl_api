from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), unique=True, index=True)
    img = Column(String(300))
    link = Column(String(300))

    books = relationship("AuthorBooks", back_populates="author")

class AuthorBooks(Base):
    __tablename__ = "author_books"

    book_id = Column(Integer, ForeignKey("book.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"), primary_key=True)

    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), unique=True, index=True)
    descr = Column(String(2000))
    img = Column(String(300))

    authors = relationship("AuthorBooks", back_populates="book")
    download_links = relationship("DownloadLink", back_populates="book")
    buy_links = relationship("BuyLink", back_populates="book")
    audio_links = relationship("AudioLink", back_populates="book")
    book_lists = relationship("ListBooks", back_populates="book")

class ListBooks(Base):
    __tablename__ = "list_books"

    book_id = Column(Integer, ForeignKey("book.id"), primary_key=True)
    book_list_id = Column(Integer, ForeignKey("book_list.id"), primary_key=True)

    book_list = relationship("BookList", back_populates="books")
    book = relationship("Book", back_populates="book_lists")

class BookList(Base):
    __tablename__ = "book_list"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), unique=True, index=True)
    is_free = Column(Boolean)

    books = relationship("ListBooks", back_populates="book_list")
    users = relationship("UserList", back_populates="book_list")

class UserList(Base):
    __tablename__ = "user_list"

    book_list_id = Column(Integer, ForeignKey("book_list.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    book_list = relationship("BookList", back_populates="users")
    user = relationship("User", back_populates="book_lists")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    os_type = Column(Integer)                               # 0 - Android, 1 - IOS
    email = Column(String(320), index=True)

    book_lists = relationship("UserList", back_populates="user")

class DownloadLink(Base):
    __tablename__ = "download_link"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(2048))
    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("Book", back_populates="download_links")

class BuyLink(Base):
    __tablename__ = "buy_link"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(2048))
    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("Book", back_populates="buy_links")

class AudioLink(Base):
    __tablename__ = "audio_link"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(2048))
    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("Book", back_populates="audio_links")




if __name__ == '__main__':
    main()
