from fastapi import Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.db import db_helper
from app.schemas.book_schema import BookSchema


async def book_by_id(book_id: int,
                     session: AsyncSession = Depends(db_helper.session_dependency)) -> BookSchema:
    book = await crud.get_book_by_id(session=session, book_id=book_id)
    if book is not None:
        return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Book {book_id} not found')
