from pydantic import BaseModel, field_validator, RootModel
from typing import List, Dict


#GET printed forms
class PrintedFormsItems(BaseModel):
    id: int
    createDataTime: str
    updateDataTime: str
    baseFileUrl: str
    fileUrl: str
    documentType: str
    name: str

    @field_validator("id", "createDataTime", "updateDataTime", "baseFileUrl", "fileUrl", "documentType", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
    
class PrintedFormsData(BaseModel):
    items: List[PrintedFormsItems]
    totalCount: int

    @field_validator("items", "totalCount")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
    
class PrintedFormsModel(BaseModel):
    message: str
    innerMessage: str | None
    data: PrintedFormsData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value



'''Create printed forms'''
class CreateData(BaseModel):
    id: int
    createDataTime: str
    updateDataTime: str
    baseFileUrl: str
    fileUrl: str
    documentType: str
    name: str

    @field_validator("id", "createDataTime", "updateDataTime", "baseFileUrl", "fileUrl", "documentType", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
    
class CreateFormsModel(BaseModel):
    message: str
    innerMessage: str | None
    data: CreateData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value



#GET placeholder
class PlaceholderFields(BaseModel):
    label: str
    key: str

    @field_validator("label", "key")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value


class PlaceholderSection(BaseModel):
    title: str
    fields: List[PlaceholderFields]

    @field_validator("title", "fields")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value


class PlaceholderData(RootModel[dict[str, List[PlaceholderSection]]]):
    pass


class PlaceholderModel(BaseModel):
    message: str
    innerMessage: str | None
    data: PlaceholderData

    @field_validator("message", "data")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
