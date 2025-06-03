from pydantic import BaseModel, field_validator


#Create Account
class CreateAccountData(BaseModel):
    id: int
    firstName: str
    middleName: str | None
    lastName: str
    identityNumber: str
    login: str
    phoneNumber: str
    email: str
    isNotifyEmail: bool
    language: str
    status: str
    permissions: list
    totalNotSendDocumentsCount: int


    @field_validator("id", "firstName",
                    "lastName", "identityNumber", "login", "phoneNumber",
                    "email", "isNotifyEmail", "language", "status",
                    "permissions", "totalNotSendDocumentsCount")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CreateAccountModel(BaseModel):
    message: str
    data: CreateAccountData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        

#Get Account
class GetAccountData(BaseModel):
    id: int
    firstName: str
    middleName: str | None
    lastName: str
    identityNumber: str
    login: str
    phoneNumber: str
    email: str
    isNotifyEmail: bool
    language: str
    status: str
    permissions: list
    totalNotSendDocumentsCount: int


    @field_validator("id", "firstName",
                    "lastName", "identityNumber", "login", "phoneNumber",
                    "email", "isNotifyEmail", "language", "status", "permissions", 
                    "totalNotSendDocumentsCount")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetAccountModel(BaseModel):
    message: str
    innerMessage: str | None
    data: CreateAccountData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value