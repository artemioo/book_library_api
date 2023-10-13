from fastapi import Depends, Path, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.db import db_helper
from app.schemas.book_schema import BaseBookSchema, BookCreateSchema, BookSchema, BookUpdateSchema

router = APIRouter(
    prefix='/books',
    tags=['book']
)


@router.get('/', response_model=list[BaseBookSchema])
async def get_all_books(session: AsyncSession = Depends(db_helper.session_dependency)) -> list[BaseBookSchema]:
    return await crud.get_books(session=session)


@router.get('/{book_id}/', response_model=BaseBookSchema)
async def get_books_by_id(book_id: int = Path(gt=0),
                          session: AsyncSession = Depends(db_helper.session_dependency)
    ) -> BaseBookSchema | None:
    return await crud.get_book_by_id(session=session, book_id=book_id)


@router.patch('/book_id/', response_model=BookSchema)
async def update_book(
        book_update: BookUpdateSchema,
        book: BookSchema = Depends(get_books_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_book(session=session, book_update=book_update, book=book, partially=False)

@router.post('/create/', response_model=BookSchema)
async def create_book(
        new_book: BookCreateSchema,
        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.add_book(session=session, new_book=new_book)


