from typing import Optional, Union
from pydantic import BaseModel, field_validator


class DocumentStatusModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class llcMemberTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class DocumentTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class UserStatusTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        

class PrintedFormTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class SignatureTypeModel(BaseModel):
    key: str
    value: int
    displayName: str

    @field_validator("key", "value", "displayName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        

        
class DataModel(BaseModel):
    documentStatus: list[DocumentStatusModel] 
    llcMemberType: list[llcMemberTypeModel] 
    documentType: list[DocumentTypeModel] 
    userStatusType: list[UserStatusTypeModel] 
    printedFormType: list[PrintedFormTypeModel] 
    signatureType: list[SignatureTypeModel] 
    @field_validator("documentStatus", "llcMemberType", "documentType", "userStatusType", "printedFormType", "signatureType")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CollectionsModel(BaseModel):
    message: str
    data: DataModel 
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


