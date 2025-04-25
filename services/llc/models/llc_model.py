from typing import Union
from pydantic import BaseModel, field_validator



#Create LLC
class LlcCreateModel(BaseModel):
    Message: str
    Data: str | None
    @field_validator("Message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value





#'''Get all LLCs by filter'''

class LlcItem(BaseModel):
    id: int
    name: str | None
    fullName: str | None
    edrpou: str
    members: list | None

    @field_validator("id",  "edrpou") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcData(BaseModel):
    totalCount: int
    items: list[LlcItem]

    @field_validator("totalCount", "items")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcModel(BaseModel):
    message: str
    data: LlcData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#'''Get LLC by ID'''

class LlcIdManagers(BaseModel):
    userId: int
    firstName: str
    middleName: str
    lastName: str
    identityNumber: str


    @field_validator("userId",  "firstName", "middleName", "lastName", "identityNumber")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcIdData(BaseModel):
    id: int
    name: str | None
    fullName: str | None
    edrpou: str
    managers: list[LlcIdManagers]
    members: list | None

    @field_validator("id",  "managers", "edrpou") 
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcIdModel(BaseModel):
    message: str
    data: LlcIdData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#'''Add manager to LLC'''

class AddManagerModel(BaseModel):
    message: str
    data: str | None
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



#'''Add members to LLC'''

class AddMemberModel(BaseModel):
    message: str
    data: str | None
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        

#Get my llc
class Members(BaseModel):
    roleName: str | None
    roleCode: str | None
    holderBalance: float
    llcMemberType: str
    llcMemberTypeName: str
    accountClass: str
    accountReference: str
    accountCategory: str
    accountOwnerList: str
    nameSurname: str
    nameForenames: str | None
    namePatronym: str | None
    nameIdCode: str
    countOfSignaturesForDocument: int | None
    countOfStampsForDocument: int  | None


    @field_validator("holderBalance", "llcMemberType", "llcMemberTypeName", "accountClass", "accountReference",
                       "accountCategory", "accountOwnerList", "nameSurname",
                       "nameIdCode")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class MyLlcData(BaseModel):
    id: int
    name: str
    fullName: str
    edrpou: str
    members: list[Members]

    @field_validator("id", "name", "fullName", "edrpou", "members")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class MyLlcModel(BaseModel):
    message: str
    data: list[MyLlcData]
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


