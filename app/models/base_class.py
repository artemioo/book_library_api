from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True  # даем Бд подсказку что такую модель создавать не надо

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'  # делаем чтоб название модели = назв. класса + s

    id: Mapped[int] = mapped_column(primary_key=True)