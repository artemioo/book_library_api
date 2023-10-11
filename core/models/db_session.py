from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession

from core.config import settings


class DatabaseHelper:

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(  # default settings
            bind=self.engine,
            autoflush=False,  # подготовка к коммиту
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoper_session(self):  # default settings
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    # метод который будет создавать сессию для каждого запроса, тоже default грубо говоря
    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(
    url=settings.DB_URL,  # а тут уже подставляем значения из settings
    echo=settings.DB_ECHO
)