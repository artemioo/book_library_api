from contextlib import asynccontextmanager


from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud

from app.db import db_helper
from app.schemas.book_schema import BookSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    # создаю БД/таблицы (код до подключения алембика)
    # async with db_helper.engine.begin() as connection:
    #     await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)



@app.get('/')
def home():
    return {'response': 'OK'}


# TODO: убрать это в api + router
@app.get('/books/', response_model=list[BookSchema])
async def get_all_books(session: AsyncSession = Depends(db_helper.session_dependency)) -> list[BookSchema]:
    return await crud.get_books(session=session)





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
