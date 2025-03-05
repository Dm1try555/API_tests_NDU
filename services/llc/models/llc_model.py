from typing import Optional, Union
from pydantic import BaseModel, field_validator


class LlcItemModel(BaseModel):
    id: int
    name: str
    fullName: str
    edrpou: Union[str, int]

    @field_validator("id",  "edrpou") #delete name and fullname
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcDataModel(BaseModel):
    totalCount: int
    items: list[LlcItemModel]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcModel(BaseModel):
    message: str
    data: LlcDataModel
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

