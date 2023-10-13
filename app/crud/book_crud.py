from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.schemas.book_schema import BaseBookSchema, BookCreateSchema, BookUpdateSchema


async def get_books(session: AsyncSession) -> list[BaseBookSchema]:
    stmt = select(Book).order_by(Book.id) # возвращает тип select, но не делает запрос к БД
    result: Result = await session.execute(stmt)   # выполнение самого запроса
    books = result.scalars().all()  # scalars возвращает генератор, а all() превращает в список
    return list(books)



# если нам нужно сделать более сложный запрос с доп фильтрами
# async def get_book_by_id(session: AsyncSession, book_id: int) -> BookSchema | None:
#     stmt = select(Book).filter(Book.id == book_id)
#     result: Result = await session.execute(stmt)
#     return result.scalar_one_or_none()
async def get_book_by_id(session: AsyncSession, book_id: int) -> BaseBookSchema | None:
    return await session.get(Book, book_id)


async def add_book(session: AsyncSession,
                   new_book: BookCreateSchema) -> Book:
    new_book = Book(**new_book.model_dump())
    session.add(new_book)
    await session.commit()
    return new_book


async def update_book(session: AsyncSession,
                      book_update: BookUpdateSchema,
                      book: Book,
                      partially: bool = False) -> Book:



    await session.commit()
    return book

# достать объект в бд, пройтись по полям и обновить их и сохранить