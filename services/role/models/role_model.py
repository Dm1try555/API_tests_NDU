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





# class GetKepGenerateModel(BaseModel):
#     token: str
#     hash: str
#
#     @field_validator("token", "hash")
#     def message_is_valid(cls, value):
#         if value == "" or value is None:
#             raise ValueError("Field is empty")
#         else:
#             return value
