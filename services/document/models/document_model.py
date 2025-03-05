from typing import Optional, Union
from pydantic import BaseModel, field_validator, root_validator



'''Create Document'''

class CreateDocumentData(BaseModel):
    id: int
    name: str
    documentType: str
    documentDirection: str
    documentStatus: str
    documentNumber: Optional[str] = None
    documentFromDate: Optional[str] = None
    memberId: int
    llcId: int
    capitalShareAction: str
    capitalShareLLCId: Optional[int] = None
    capitalShareSize: Optional[str] = None
    escrowAccountNumber: Optional[str] = None
    escrowDocumentNumber: Optional[str] = None
    escrowDocumentDate: Optional[str] = None
    counterpartyIdentifyNumber: Optional[str] = None
    counterpartyName: Optional[str] = None
    counterpartyDocumentNumber: Optional[str] = None
    counterpartyDocumentDate: Optional[str] = None
    counterpartyDocumentUrl: Optional[str] = None
    messageCdData: Optional[str] = None
    messageCdTopic: Optional[str] = None
    messageCdFileUrl: Optional[str] = None
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int

    @root_validator(pre=True)
    def check_empty_fields(cls, values):
        required_fields = [
            "id", "name", "documentType", "documentDirection", "documentStatus",
            "memberId", "llcId", "capitalShareAction", "countOfSignaturesForDocument", "countOfStampsForDocument"
        ]
        for field in required_fields:
            if values.get(field) is None or (isinstance(values.get(field), str) and values.get(field).strip() == ""):
                raise ValueError(f"Field '{field}' cannot be empty or None.")
        return values

    @field_validator("capitalShareLLCId", "capitalShareSize", "escrowAccountNumber", "escrowDocumentNumber",
        "escrowDocumentDate", "counterpartyIdentifyNumber", "counterpartyName",
        "counterpartyDocumentNumber", "counterpartyDocumentDate", "counterpartyDocumentUrl",
        "messageCdData", "messageCdTopic", "messageCdFileUrl")
    def check_optional_fields(cls, value, field):
        if value == "" or value is None:
            return None
        return value

class CreateDocumentModel(BaseModel):
    message: str
    data: CreateDocumentData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Delete Document'''

class DeleteDocumentModel(BaseModel):
    message: str
    data: None
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

'''Check document after Delete'''

class CheckDeleteDocumentModel(BaseModel):
    Message: str
    Data: None
    @field_validator("Message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''PUT Copy Document'''

class CopyDocumentData(BaseModel):
    id: int
    name: str
    documentType: str
    documentDirection: str
    documentStatus: str
    documentNumber: Optional[str] = None
    documentFromDate: Optional[str] = None
    memberId: int
    llcId: int
    capitalShareAction: str
    capitalShareLLCId: Optional[int] = None
    capitalShareSize: Optional[str] = None
    escrowAccountNumber: Optional[str] = None
    escrowDocumentNumber: Optional[str] = None
    escrowDocumentDate: Optional[str] = None
    counterpartyIdentifyNumber: Optional[str] = None
    counterpartyName: Optional[str] = None
    counterpartyDocumentNumber: Optional[str] = None
    counterpartyDocumentDate: Optional[str] = None
    counterpartyDocumentUrl: Optional[str] = None
    messageCdData: Optional[str] = None
    messageCdTopic: Optional[str] = None
    messageCdFileUrl: Optional[str] = None
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int

    @root_validator(pre=True)
    def check_empty_fields(cls, values):
        required_fields = [
            "id", "name", "documentType", "documentDirection", "documentStatus",
            "memberId", "llcId", "capitalShareAction", "countOfSignaturesForDocument", "countOfStampsForDocument"
        ]
        for field in required_fields:
            if values.get(field) is None or (isinstance(values.get(field), str) and values.get(field).strip() == ""):
                raise ValueError(f"Field '{field}' cannot be empty or None.")
        return values

    @field_validator("capitalShareLLCId", "capitalShareSize", "escrowAccountNumber", "escrowDocumentNumber",
        "escrowDocumentDate", "counterpartyIdentifyNumber", "counterpartyName",
        "counterpartyDocumentNumber", "counterpartyDocumentDate", "counterpartyDocumentUrl",
        "messageCdData", "messageCdTopic", "messageCdFileUrl")
    def check_optional_fields(cls, value, field):
        if value == "" or value is None:
            return None
        return value

class CopyDocumentModel(BaseModel):
    message: str
    data: CreateDocumentData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

'''GET Audit Document'''

class AuditDocumentItemModel(BaseModel):
    id: int
    createdBy: str
    createDataTime: str
    description: str

    @field_validator("id", "description", "createDataTime", "createdBy")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class AuditDocumentDataModel(BaseModel):
    totalCount: int
    items: list[AuditDocumentItemModel]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AuditDocumentModel(BaseModel):
    message: str
    data: AuditDocumentDataModel
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value





# '''Get Document'''
#
# class GetDocumentItemModel(BaseModel):
#     id: int
#     name: str
#     createDataTime: str
#     memberName: str
#     llcName: str
#     llcedrpou: str
#     documentStatus: str
#
#     @field_validator("id", "name", "createDataTime", "memberName", "llcName", "llcedrpou", "documentStatus")
#     def fields_are_valid(cls, value):
#         if value == "" or value is None:
#             raise ValueError("Field is empty")
#         else:
#             return value
#
#
# class GetDocumentDataModel(BaseModel):
#     totalCount: int
#     items: list[GetDocumentItemModel]
#
#     @field_validator("totalCount")
#     def total_count_is_valid(cls, value):
#         if value == "" or value is None:
#             raise ValueError("Field is empty")
#         else:
#             return value
#
# class GetDocumentModel(BaseModel):
#     message: str
#     data: GetDocumentDataModel
#     @field_validator("message")
#     def message_is_valid(cls, value):
#         if value == "" or value is None:
#             raise ValueError("Field is empty")
#         else:
#             return value

