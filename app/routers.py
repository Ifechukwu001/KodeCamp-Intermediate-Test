from fastapi import APIRouter, HTTPException

from . import models
from . import schema

router = APIRouter()


@router.get("/", response_model=list[schema.BookInMem])
async def get_books():
    books = [book for book in models.Book.values()]
    return books


@router.post("/", response_model=schema.BookInMem, status_code=201)
async def create_book(book: schema.Book):
    id = next(models.id)
    book_data = book.model_dump()
    book_data["id"] = id
    models.Book[id] = book_data
    book = schema.BookInMem(**book_data)
    return book


@router.get("/{id}", response_model=schema.BookInMem)
async def get_book(id: int):
    book = models.Book.get(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/{id}", response_model=schema.BookInMem)
async def update_book(id: int, book: schema.BookUpdate):
    mem_book = models.Book.get(id)
    if not mem_book:
        raise HTTPException(status_code=404, detail="Book not found")
    book_data = book.model_dump()
    for key, value in book_data.items():
        if value:
            mem_book[key] = value
    book = schema.BookInMem(**mem_book)
    return book


@router.delete("/{id}", status_code=200)
async def delete_book(id: int):
    book = models.Book.pop(id, None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
