from pydantic import BaseModel, field_validator




#'Get Signature System'
class GetSignatureItemModel(BaseModel):
    id: int
    name: str
    llcId: int | None
    createdOn: str
    identifier: str | None
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    isDefaultPhysicalPerson: bool
    isDefaultJuridicalPerson: bool

    @field_validator("id", "name", "createdOn", "countOfSignaturesForDocument", "countOfStampsForDocument", "isDefaultPhysicalPerson", "isDefaultJuridicalPerson")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetSignatureData(BaseModel):
    totalCount: int
    items: list[GetSignatureItemModel]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetSignatureModel(BaseModel):
    message: str
    data: GetSignatureData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#'Get Signature by ID'
class GetSignatureByIdModel(BaseModel):
    message: str
    data: GetSignatureItemModel

    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value




#'Create Signature System'
class CreateSignatureData(BaseModel):
    id: int
    name: str
    llcId: int
    createdOn: str
    identifier: str
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    isDefaultPhysicalPerson: bool
    isDefaultJuridicalPerson: bool

    @field_validator("id", "name", "llcId", "createdOn", "identifier", "countOfSignaturesForDocument",
                     "countOfStampsForDocument", "isDefaultPhysicalPerson", "isDefaultJuridicalPerson")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CreateSignatureModel(BaseModel):
    message: str
    data: CreateSignatureData

    @field_validator("message", "data")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value




#'Change Signature System'
class ChangeSignatureData(BaseModel):
    id: int
    name: str
    llcId: int | None
    createdOn: str
    identifier: str | None
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    isDefaultPhysicalPerson: bool
    isDefaultJuridicalPerson: bool

    @field_validator("id", "name", "createdOn", "countOfSignaturesForDocument",
                     "countOfStampsForDocument", "isDefaultPhysicalPerson", "isDefaultJuridicalPerson")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class ChangeSignatureModel(BaseModel):
    message: str
    data: ChangeSignatureData

    @field_validator("message", "data")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#'Delete Signature System'
class DeleteSignatureModel(BaseModel):
    message: str
    data: str | None

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
