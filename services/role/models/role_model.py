from typing import Union
from pydantic import BaseModel, field_validator



class CreateRoleData(BaseModel):
    id: int
    name: str
    isAdminPart: bool
    dependCodes: list[str]
    description: str
    createdDate: str
    permissions: list[str]

    @field_validator("id", "name", "isAdminPart", "dependCodes", "description",
                     "createdDate", "permissions" )
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CreateRoleModel(BaseModel):
    message: str
    data: CreateRoleData

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetRoleData(BaseModel):
    id: int
    name: str
    isAdminPart: bool
    dependCodes: list[str]
    description: str
    createdDate: str
    permissions: list[str]

    @field_validator("id", "name", "isAdminPart", "dependCodes", "description",
                     "createdDate", "permissions" )
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetRoleModel(BaseModel):
    message: Union[str, None]
    data: GetRoleData

    @field_validator("data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



class ChangeRoleData(BaseModel):
    id: int
    name: str
    isAdminPart: bool
    dependCodes: list[str]
    description: str
    createdDate: str
    permissions: list[str]

    @field_validator("id", "name", "isAdminPart", "dependCodes", "description",
                     "createdDate", "permissions" )
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class ChangeRoleModel(BaseModel):
    message: str
    data: CreateRoleData

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetRolePermissionsModel(BaseModel):
    message: str
    data: list[str]

    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetRoleFiltersItem(BaseModel):
    id: int
    name: str
    dependCodes: list[str]
    description: str
    createdDate: str

    @field_validator("id", "name", "dependCodes", "description",
                     "createdDate" )
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetRoleFiltersData(BaseModel):
    totalCount: int
    items: list[GetRoleFiltersItem]

    @field_validator("totalCount")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetRoleFiltersModel(BaseModel):
    message: Union[str, None]
    data: GetRoleFiltersData

    @field_validator("data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value