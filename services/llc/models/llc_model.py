from typing import Union
from pydantic import BaseModel, field_validator

'''Get all LLC'''

class LlcItem(BaseModel):
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

class LlcData(BaseModel):
    totalCount: int
    items: list[LlcItem]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcModel(BaseModel):
    message: str
    data: LlcData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Get LLC by id'''

class LlcIdManagers(BaseModel):
    userId: int
    firstName: str
    middleName: str
    lastName: str
    identityNumber: str


    @field_validator("userId",  "firstName", "middleName", "lastName", "identityNumber")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcIdData(BaseModel):
    id: int
    name: str
    fullName: str
    edrpou: str
    managers: list[LlcIdManagers]
    members: list | None

    @field_validator("id",  "managers", "name", "fullName", "edrpou") #"members"
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcIdModel(BaseModel):
    message: str
    data: LlcIdData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Add manager to LLC'''

class AddManagerModel(BaseModel):
    message: str
    data: str | None
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

