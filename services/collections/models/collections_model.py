from typing import Optional, Union
from pydantic import BaseModel, field_validator


class CollectionsDocumentStatusModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CollectionsMemberTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CollectionsDocumentTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CollectionsModel(BaseModel):
    message: str
    data: dict[str, list[Union[CollectionsDocumentStatusModel, CollectionsMemberTypeModel, CollectionsDocumentTypeModel]]]

    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


