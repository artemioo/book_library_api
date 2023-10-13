from fastapi import APIRouter
from .endpoints import book_router

api_router = APIRouter()

api_router.include_router(book_router)