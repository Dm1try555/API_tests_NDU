from typing import Optional, Union
from pydantic import BaseModel, field_validator

#Наш ответ: Проверяет наличие поле и его тип данных
#Create user
class AdminUserModel(BaseModel):
    id: int
    firstName: str
    middleName: Optional[str] = None
    lastName: str
    identityNumber: Union[str, int]
    login: Union[str, int]
    phoneNumber: Optional[str] = None
    email: Optional[str] = None
    isNotifyEmail: bool = False
    language: str
    status: str


    @field_validator("id", "firstName", "lastName", "identityNumber", "login", "isNotifyEmail", "language", "status")
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

    @field_validator("id", "createdBy", "createDataTime", "description")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AdminUserAuditData(BaseModel):
    totalCount: int
    items: list[AdminUserAuditItem]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AdminUserAuditModel(BaseModel):
    message: str
    data: AdminUserAuditData

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



class AdminUserPassword(BaseModel):
    message: str
    data: None

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value