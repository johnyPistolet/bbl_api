from typing import List, Optional
from pydantic import BaseModel



class DownloadLinkBase(BaseModel):
    link: str
    book_id: int

class DownloadLinkCreate(DownloadLinkBase):
    pass

class DownloadLink(DownloadLinkBase):
    id: int

    class Config:
            orm_mode = True



class BuyLinkBase(BaseModel):
    link: str
    book_id: int

class BuyLinkCreate(BuyLinkBase):
    pass

class BuyLink(BuyLinkBase):
    id: int

    class Config:
            orm_mode = True



class AudioLinkBase(BaseModel):
    link: str
    book_id: int

class AudioLinkCreate(AudioLinkBase):
    pass

class AudioLink(AudioLinkBase):
    id: int

    class Config:
            orm_mode = True

class AuthorBase(BaseModel):
    name: str
    img: Optional[str] = None
    link: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
            orm_mode = True



class BookBase(BaseModel):
    title: str
    descr: str
    img: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    authors: List[Author] = []
    download_links: List[DownloadLink] = []
    buy_links: List[BuyLink] = []
    audio_links: List[AudioLink] = []

    class Config:
            orm_mode = True




class BookListBase(BaseModel):
    title: str
    is_free: bool

class BookListCreate(BookListBase):
    pass

class BookList(BookListBase):
    id: int
    books: List[Book] = []

    class Config:
            orm_mode = True


class UserBase(BaseModel):
    email: str
    os_type: int                                # 0 - Android, 1 - IOS

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    book_lists: List[BookList] = []

    class Config:
            orm_mode = True



class UserListBase(BaseModel):
    user_id: int
    book_list_id: int

class UserListCreate(UserListBase):
    pass

class UserList(UserListBase):
    user: User
    book_list: BookList

    class Config:
            orm_mode = True



class ListBooksBase(BaseModel):
    book_id: int
    book_list_id: int

class ListBooksCreate(ListBooksBase):
    pass

class ListBooks(ListBooksBase):
    book_list: BookList
    book: Book

    class Config:
            orm_mode = True





class AuthorBooksBase(BaseModel):
    book_id: int
    author_id: int

class AuthorBooksCreate(AuthorBooksBase):
    pass

class AuthorBooks(AuthorBooksBase):
    book: Book
    author: Author

    class Config:
            orm_mode = True



if __name__ == '__main__':
    main()