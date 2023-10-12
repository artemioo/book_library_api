from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.schemas.book_schema import BookSchema


async def get_books(session: AsyncSession) -> list[BookSchema]:
    stmt = select(Book).order_by(Book.id)
    result: Result = await session.execute(stmt)   # Result это аннотация типа
    books = result.scalars().all()  #
    return list(books)
