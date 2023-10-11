from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.models import Base
from core.models.db_session import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # создаю БД/таблицы (код до подключения алембика)
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)



@app.get('/')
def home():
    return {'response': 'OK'}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
