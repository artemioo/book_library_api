from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base_class import Base

from enum import Enum


# class Language(Enum):
#     english = 'english'
#     ukrainian = 'ukrainian'


class Book(Base):
    title: Mapped[str] = mapped_column(String(200), unique=False)
    year: Mapped[int] = mapped_column(Integer)
    pages: Mapped[int]
    # language:
    #author
    #series
    # genre
    # category
    # pages
    # language
    def __str__(self):
        return f'(id={self.id}, username={self.title!r})'

    def __repr__(self):
        return str(self)
