from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    publication: int
    genre: str


class BookUpdate(Book):
    title: str = None
    author: str = None
    publication: int = None
    genre: str = None


class BookInMem(Book):
    id: int
