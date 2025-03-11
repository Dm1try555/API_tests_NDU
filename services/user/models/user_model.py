from typing import Optional, Union
from pydantic import BaseModel, field_validator


'''GET User'''

class GetUserRoles(BaseModel):
    id: int
    name: str

    @field_validator("id", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetUserItem(BaseModel):
    id: int
    firstName: str
    middleName: Union[str, None]
    lastName: str
    identityNumber: str
    login: str
    creationTime: str
    status: str
    roles: list[GetUserRoles]

    @field_validator("id", "firstName", "lastName", "identityNumber", "login", "creationTime", "roles", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetUserData(BaseModel):
    totalCount: int
    items: list[GetUserItem]

    @field_validator("totalCount", "items")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetUserModel(BaseModel):
    message: str
    data: GetUserData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value




'''POST User'''

class CreateUserData(BaseModel):

    id: int
    firstName: str
    middleName: str
    lastName: str
    identityNumber: str
    login: str
    phoneNumber: Union[str, None]
    email: Union[str, None]
    isNotifyEmail: bool
    language: str
    status: str

    @field_validator("id", "firstName", "middleName", "lastName", "identityNumber", "login", "isNotifyEmail", "language", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CreateUserModel(BaseModel):

    message: str
    data: CreateUserData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



'''Change status'''

class StatusModel(BaseModel):
    message: str
    data: Union[str,None]

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



'''GET Audit'''

class UserAuditItem(BaseModel):
    id: int
    createdBy: str
    createDataTime: str
    description: str

    @field_validator("id", "createdBy", "createDataTime", "description")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class UserAuditData(BaseModel):
    totalCount: int
    items: list[UserAuditItem]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class UserAuditModel(BaseModel):
    message: str
    data: UserAuditData

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''GET User by ID'''

class GetUserIdRoles(BaseModel):
    id: int
    name: str

    @field_validator("id", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetUserIdData(BaseModel):
    id: int
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    identityNumber: str
    login: str
    language: str
    isNotifyEmail: bool
    countOfSignaturesForDocument: Optional[str] = None
    countOfStampsForDocument: Optional[str] = None
    status: str
    lastLoginTime: Optional[str] = None
    lastPasswordChangeTime: Optional[str] = None
    creationTime: str
    updatedTime: str
    roles: list[GetUserIdRoles]


    @field_validator("id", "firstName", "lastName", "identityNumber", "login",
                     "isNotifyEmail", "language", "status", "creationTime", "updatedTime")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetUserIdModel(BaseModel):
    message: str
    data: GetUserData

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
