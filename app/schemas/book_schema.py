from pydantic import Field, BaseModel, ConfigDict


class BookSchema(BaseModel):
    title: str = Field(min_length=1)
    year: int = Field(gt=0)
    pages: int = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)  # ???
