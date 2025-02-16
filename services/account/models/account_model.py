from pydantic import BaseModel, field_validator


class AccountModel(BaseModel):
    id: int
    firstName: str
    middleName: str
    lastName: str
    identityNumber: int
    login: int
    phoneNumber: int
    email: str
    isNotifyEmail: bool = True
    language: str
    status: str


    @field_validator("id", "firstName", "middleName", "lastName", "identityNumber", "login", "phoneNumber", "email", "isNotifyEmail", "language", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value