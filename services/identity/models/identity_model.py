from typing import Optional, Union
from pydantic import BaseModel, field_validator

'''Auth'''

class AuthDataModel(BaseModel):
    id: int
    userName: str
    email: str
    roles: list[str]
    isVerified: bool = False
    accessToken: str
    refreshToken: str


    @field_validator("id", "userName", "email", "roles", "isVerified", "accessToken", "refreshToken")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class AuthModel(BaseModel):
    message: str
    data: Optional[AuthDataModel]

    @field_validator("message", "data")
    def message_and_data_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

'''Auth code'''

class AuthCodeModel(BaseModel):
    token: str

    @field_validator("token")
    def message_and_data_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Change Password'''

class ChangePasswordModel(BaseModel):
    message: str
    data: Optional[None]

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Get Hash'''

class GetHashModel(BaseModel):
    message: str
    data: str

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


# class RefreshTokenModel(BaseModel):
#     Message: str
#     Data: Optional[None]
#
#     @field_validator("message")
#     def fields_are_not_empty(cls, value):
#         if value == "" or value is None:
#             raise ValueError("Field is empty")
#         else:
#             return value