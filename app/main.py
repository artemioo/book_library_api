from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from app.api.v1.api import api_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # создаю БД/таблицы (код до подключения алембика)
    # async with db_helper.engine.begin() as connection:
    #     await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get('/')
def home():
    return {'response': 'OK'}


# TODO: убрать это в api + router





if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
