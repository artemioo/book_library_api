from fastapi import Depends, Path, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.db import db_helper
from app.deps.book_deps import book_by_id
from app.schemas.book_schema import BaseBookSchema, BookCreateSchema, BookSchema, BookUpdateSchema, \
    BookUpdatePartialSchema

router = APIRouter(
    prefix='/books',
    tags=['book']
)


@router.get('/', response_model=list[BaseBookSchema])
async def get_all_books(session: AsyncSession = Depends(db_helper.session_dependency)) -> list[BaseBookSchema]:
    return await crud.get_books(session=session)


@router.get('/{book_id}/', response_model=BookSchema)
async def get_book(book: BookSchema = Depends(book_by_id)):
    return book


@router.patch('/book_id/')
async def update_book_partial(
        book_update: BookUpdatePartialSchema,
        book: BookSchema = Depends(book_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True)

@router.put('/book_id/')
async def update_book(
        book_update: BookUpdateSchema,
        book: BookSchema = Depends(book_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=False)





@router.post('/create/', response_model=BookSchema)
async def create_book(
        new_book: BookCreateSchema,
        session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.add_book(session=session, new_book=new_book)


