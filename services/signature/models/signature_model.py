from typing import Optional, Union
from pydantic import BaseModel, field_validator


class SignatureItemModel(BaseModel):
    id: int
    name: str
    llcId: Optional[int]
    createdOn: str
    identifier: Optional[str]
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    isDefaultPhysicalPerson: bool = False
    isDefaultJuridicalPerson: bool = False

    @field_validator("id", "name", "createdOn", "countOfSignaturesForDocument", "countOfStampsForDocument", "isDefaultPhysicalPerson", "isDefaultJuridicalPerson")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class SignatureDataModel(BaseModel):
    totalCount: int
    items: list[SignatureItemModel]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class SignatureModel(BaseModel):
    message: str
    data: SignatureDataModel
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class SignatureByIdModel(BaseModel):
    message: str
    data: SignatureItemModel

