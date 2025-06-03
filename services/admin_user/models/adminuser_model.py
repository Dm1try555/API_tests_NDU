from typing import Optional, Union
from pydantic import BaseModel, field_validator


class GetAdminUserRoles(BaseModel):
    id: int
    name: str

    @field_validator("id", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetAdminUserItem(BaseModel):
    id: int
    firstName: str
    middleName: str | None
    lastName: str
    identityNumber: str
    login: str
    creationTime: str
    status: str
    roles: list[GetAdminUserRoles]

    @field_validator("id", "firstName", "lastName", "identityNumber", "login", "creationTime", "roles", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetAdminUserData(BaseModel):
    totalCount: int
    totalNotSendDocumentsCount: int
    items: list[GetAdminUserItem]

    @field_validator("totalCount", "items", "totalNotSendDocumentsCount")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetAdminUserModel(BaseModel):
    message: str
    innerMessage: str | None
    data: GetAdminUserData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value





class CreateAdminUserData(BaseModel):
    id: int
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    identityNumber: Union[str, int]
    login: Union[str, int]
    phoneNumber: Optional[str] = None
    email: Optional[str] = None
    isNotifyEmail: bool
    language: str
    status: str


    @field_validator("id", "firstName", "lastName", "identityNumber", "login", "isNotifyEmail", "language", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CreateAdminUserModel(BaseModel):
    message: str
    data: CreateAdminUserData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class StatusModel(BaseModel):
    message: str
    data: Union[str,None]

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#AUDIT
class AdminUserAuditItem(BaseModel):
    id: int
    createdBy: str
    createDataTime: str
    description: str
    documentStatus: str

    @field_validator("id", "createdBy", "createDataTime", "description", "documentStatus")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AdminUserAuditData(BaseModel):
    totalCount: int
    items: list[AdminUserAuditItem]

    @field_validator("totalCount", "items")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AdminUserAuditModel(BaseModel):
    message: str
    data: AdminUserAuditData

    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#CHANGE PASSWORD
class AdminUserPassword(BaseModel):
    message: str
    data: None

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#CHANGE ROLES
class ChangeAdminUserRoles(BaseModel):
    id: int
    name: str

    @field_validator("id", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

#CHANGE USER
class ChangeAdminUserData(BaseModel):
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
    roles: Optional[list[ChangeAdminUserRoles]] = None


    @field_validator("id", "firstName", "lastName", "identityNumber", "login",
                     "isNotifyEmail", "language", "status", "creationTime", "updatedTime")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class ChangeAdminUserModel(BaseModel):
    message: str
    data: ChangeAdminUserData

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value