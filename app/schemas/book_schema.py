from pydantic import Field, BaseModel, ConfigDict


class BaseBookSchema(BaseModel):
    title: str = Field(min_length=1)
    year: int = Field(gt=0)
    pages: int = Field(gt=0)


class BookCreateSchema(BaseBookSchema):
    pass


class BookUpdateSchema(BaseBookSchema):
    pass


class BookUpdatePartialSchema(BaseModel):
    title: str | None = None
    year: int | None = None
    pages: int | None = None
# TODO сделать валидатор для этих полей

class BookSchema(BaseBookSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int