from pydantic import BaseModel, field_validator


class CreateAccountData(BaseModel):
    id: int
    firstName: str
    middleName: str
    lastName: str
    identityNumber: str
    login: str
    phoneNumber: str
    email: str
    isNotifyEmail: bool = True
    language: str
    status: str


    @field_validator("id", "firstName", "middleName",
                     "lastName", "identityNumber", "login", "phoneNumber",
                     "email", "isNotifyEmail", "language", "status")
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