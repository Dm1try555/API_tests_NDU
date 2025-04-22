from typing import Optional, Union
from pydantic import BaseModel, field_validator

# UserModel
class GetUserItem(BaseModel):
    id: int
    firstName: str
    middleName: Union[str, None]
    lastName: str
    identityNumber: str
    login: str
    creationTime: str
    status: str

    @field_validator("id", "firstName", "lastName", "identityNumber", "login", "creationTime", "status")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetUserData(BaseModel):
    totalCount: int
    items: list[GetUserItem]

    @field_validator("totalCount")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetUserModel(BaseModel):
    message: str
    data: GetUserData

    @field_validator("message")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



#CounterAgentModel
class CounterAgentData(BaseModel):
    identityNumber: str
    fullName: str

    @field_validator("identityNumber", "fullName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CounterAgentModel(BaseModel):
    message: str
    data: list[CounterAgentData]

    @field_validator("message", "data")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value




