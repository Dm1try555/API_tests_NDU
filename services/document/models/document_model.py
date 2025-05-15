from typing import Optional, Union
from pydantic import BaseModel, field_validator, root_validator, model_validator

'''Create Document'''

class CreateDocumentData(BaseModel):
    id: int
    name: str
    documentType: str
    documentDirection: str
    documentStatus: str
    llcMemberType: str
    roleName: str | None
    roleCode: str | None
    outNum: str | None
    outDate: str | None
    isPresentOutNum: bool
    memberAccountReference: str | None 
    memberDocumentNumber: str | None
    llcId: int
    clientName: str
    clientFullName: str
    clientCode: str
    shareSize: str | None
    isFullShareSize: bool
    capitalShareAction: str | None
    counterPartyCode: str | None
    counterPartyName: str | None
    nameBlockFor: str | None
    codeBlockFor: str | None
    capitalShareLLCId: str | None
    escrowAccountNumber: str | None
    escrowDocumentNumber: str | None
    escrowDocumentDate: str | None
    contractNum: str | None
    contractDate: str | None
    messageCdData: str | None
    messageCdTopic: str | None
    messageCdFileUrl: str | None

    countOfSignaturesForDocument: int
    countOfStampsForDocument: int


    p_DocumentName: str 


    @field_validator("id", "name", "documentType", "documentDirection", "documentStatus",
                     "llcMemberType", 
                     "llcId", "clientName", "clientFullName",
                     "clientCode", "isPresentOutNum",
                     "countOfSignaturesForDocument", "countOfStampsForDocument",
                     "p_DocumentName")
    @classmethod
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CreateDocumentModel(BaseModel):
    message: str
    data: CreateDocumentData

    @field_validator("message")
    @classmethod
    def message_is_valid(cls, value):
        if not value.strip():
            raise ValueError("Field 'message' cannot be empty")
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
    llcMemberType: str
    roleName: str | None
    roleCode: str | None
    outNum: str | None
    outDate: str | None
    isPresentOutNum: bool
    memberAccountReference: str | None
    memberDocumentNumber: str | None
    llcId: int
    clientName: str | None
    clientFullName: str | None
    clientCode: str | None
    memberRoles: str | None
    shareSize: str | None
    isFullShareSize: bool
    capitalShareAction: str | None
    counterPartyCode: str | None
    counterPartyName: str | None
    nameBlockFor: str | None
    codeBlockFor: str | None
    blockReasonNameOther: str | None
    capitalShareLLCId: str | None
    escrowAccountNumber: str | None
    escrowDocumentNumber: str | None
    escrowDocumentDate: str | None
    contractNum: str | None
    contractDate: str | None
    holderBalance: str | None
    accountClass: str | None
    messageCdData: str | None
    messageCdTopic: str | None
    messageCdFileUrl: str | None
    signatures: str | None
    files: str | None
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    p_Surname: str | None
    p_Name: str | None
    p_Secondname: str | None
    p_Code: str | None
    p_IsCodeExist: bool
    p_CodeEDDR: str | None
    p_Citizenship: str | None
    p_BirthPlace: str | None
    p_DocumentName: str 
    p_DocumentNumber_Series: str | None
    p_DocumentNumber: str | None
    p_DocumentDate: str | None
    p_DocumentWho: str | None
    p_BirthDate: str | None
    p_Country: str | None
    p_Region: str | None
    p_City: str | None
    p_Address: str | None
    p_PostIndex: str | None
    p_Is_Mailing_Address_Matches_Location: bool
    p_CodeTerUnit: str | None
    p_TaxResidencyStatusResName: bool
    p_IsFOP: bool
    p_FOPAuthority: str | None
    p_PostAddress: str | None
    p_Phone: str | None
    p_MobilePhone: str | None
    p_Email: str | None
    p_ContractNum: str | None
    p_ContractDate: str | None
    p_EmailSend: str | None
    p_BankName: str | None
    p_BankMFO: str | None
    p_BankAccount: str | None
    mg_Name: str | None
    mg_Code: str | None
    mg_IsJur: str | None
    mg_AuthDocument: str | None
    mg_TermAuthority: str | None
    mg_DocumentNumber_Series: str | None
    mg_DocumentNumber: str | None
    firstPersonName: str | None
    firstPersonCode: str | None
    firstPersonCode_DocumentNumber_Series: str | None
    firstPersonCode_DocumentNumber: str | None
    firstPersonPosition: str | None
    f_DocumentInfo: str | None
    f_TermAuthority: str | None
    managerList: list
    representList: list
    jurNonResidentName: str | None
    jurNonResidentShortName: str | None
    jurNonResidentCode: str | None
    jurNonResidentRegCountry: str | None
    p_TaxResidencyStatusResOwnersName: bool
    jurName: str | None
    jurShortName: str | None
    jurShortNameEng: str | None
    jurEdrpou: str | None
    jurEdrisi: str | None
    jurRegCountry: str | None
    govName: str | None
    govShortName: str | None
    govCode: str | None
    letterDepository: str | None

    @field_validator("id", "name", "documentType", "documentDirection", "documentStatus", "llcMemberType", "isPresentOutNum", "llcId", "isFullShareSize", "countOfSignaturesForDocument", "countOfStampsForDocument",
                    "p_IsCodeExist", "p_DocumentName", "p_Is_Mailing_Address_Matches_Location", "p_TaxResidencyStatusResName", "p_TaxResidencyStatusResOwnersName")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CopyDocumentModel(BaseModel):
    message: str
    data: CopyDocumentData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

'''GET Audit Document'''

class AuditDocumentItem(BaseModel):
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


class AuditDocumentData(BaseModel):
    totalCount: int
    items: list[AuditDocumentItem]

    @field_validator("totalCount")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class AuditDocumentModel(BaseModel):
    message: str
    data: AuditDocumentData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value




'''Get Document'''

class GetDocumentItem(BaseModel):
    id: int
    name: str
    createDataTime: str
    memberName: str
    llcName: str | None
    llcedrpou: str
    documentStatus: str

    @field_validator("id", "name", "createDataTime", "memberName", "llcedrpou", "documentStatus")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class GetDocumentData(BaseModel):
    totalCount: int
    items: list[GetDocumentItem]

    @field_validator("totalCount", "items")
    def total_count_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetDocumentModel(BaseModel):
    message: str
    data: GetDocumentData
    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

#Upload Document

class Files(BaseModel):
    id: str
    fileName: str
    contentType: str
    fileSize: str
    url: str
    extension: str
    isTemplate: bool
    printedFileType: str
    creationDate: str
    hash: str

    @field_validator("id", "fileName", "contentType", "fileSize", "url",
                    "extension", "isTemplate", "printedFileType", "creationDate", "hash")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class UploadDocumentData(BaseModel):
    id: int
    name: str
    documentType: str
    documentDirection: str
    documentStatus: str
    llcMemberType: str
    roleName: str | None
    roleCode: str | None
    outNum: str 
    outDate: str
    isPresentOutNum: bool
    memberAccountReference: str
    memberDocumentNumber: str | None
    llcId: int
    clientName: str
    clientFullName: str
    clientCode: str
    memberRoles: str
    shareSize: int
    isFullShareSize: bool
    capitalShareAction: str
    counterPartyCode: str 
    counterPartyName: str
    nameBlockFor: str | None
    codeBlockFor: str | None
    blockReasonNameOther: str | None
    capitalShareLLCId: str | None
    escrowAccountNumber: str | None
    escrowDocumentNumber: str | None
    escrowDocumentDate: str | None
    contractNumber: str 
    contractDate: str 
    holderBalance: str | None
    accountClass: str | None
    messageCdData: str | None
    messageCdTopic: str | None
    messageCdFileUrl: str | None
    signatures: list
    files: list[Files]
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    p_Surname: str | None
    p_Name: str | None
    p_Secondname: str | None
    p_Code: str | None
    p_IsCodeExist: bool
    p_CodeEDDR: str | None
    p_Citizenship: str
    p_BirthPlace: str | None
    p_DocumentName: str
    p_DocumentNumber_Series: str | None
    p_DocumentNumber: str | None
    p_DocumentDate: str | None
    p_DocumentWho: str | None
    p_BirthDate: str | None
    p_Country: str
    p_Region: str | None
    p_City: str | None
    p_Address: str | None
    p_PostIndex: str | None
    p_Is_Mailing_Address_Matches_Location: bool
    p_CodeTerUnit: str | None
    p_TaxResidencyStatusResName: bool
    p_IsFOP: bool
    p_FOPAuthority: str | None
    p_PostAddress: str | None
    p_Phone: str | None
    p_MobilePhone: str | None
    p_Email: str | None
    p_ContractNum: str | None
    p_ContractDate: str | None
    p_EmailSend: str | None
    p_BankName: str | None
    p_BankMFO: str | None
    p_BankAccount: str | None
    mg_Name: str
    mg_Code: str
    mg_IsJur: str | None
    mg_AuthDocument: str | None
    mg_TermAuthority: str | None
    mg_DocumentNumber_Series: str | None
    mg_DocumentNumber: str | None
    firstPersonName: str | None
    firstPersonCode: str | None
    firstPersonCode_DocumentNumber_Series: str | None
    firstPersonCode_DocumentNumber: str | None
    firstPersonPosition: str | None
    f_DocumentInfo: str | None
    f_TermAuthority: str | None
    managerList: list
    representList: list
    jurNonResidentName: str | None
    jurNonResidentShortName: str | None
    jurNonResidentCode: str | None
    jurNonResidentRegCountry: str | None
    p_TaxResidencyStatusResOwnersName: bool
    jurName: str | None
    jurShortName: str | None
    jurShortNameEng: str | None
    jurEdrpou: str | None
    jurEdrisi: str | None
    jurRegCountry: str | None
    govName: str
    govShortName: str | None
    govCode: str
    letterDepository: str | None

    @field_validator(
    "id", "name", "documentType", "documentDirection", "documentStatus",
    "llcMemberType", "outNum", "outDate", "isPresentOutNum", "memberAccountReference",
    "llcId", "shareSize", "capitalShareAction", "counterPartyCode", "counterPartyName",
    "contractNum", "contractDate", "files", "countOfSignaturesForDocument",
    "countOfStampsForDocument", "p_Citizenship", "p_DocumentName", "p_Country",
    "p_Is_Mailing_Address_Matches_Location", "p_TaxResidencyStatusResName", "p_IsFOP",
    "mg_Name", "mg_Code", "p_TaxResidencyStatusResOwnersName", "govName", "govCode")
    def validate_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value

class UpdateDocumentModel(BaseModel):
    message: str
    data: UploadDocumentData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


#Change Document
class ChangeManagerList(BaseModel):
    m_Name: str
    m_Code: str
    m_DocumentName: str
    m_DocumentSerial: str
    m_DocumentNumber: str
    m_DocumentDate: str
    m_DocumentWho: str
    m_AuthDocument: str
    m_TermAuthority: str

    @field_validator(
    "m_Name", "m_Code", "m_DocumentName", "m_DocumentSerial", "m_DocumentNumber",
    "m_DocumentDate", "m_DocumentWho", "m_AuthDocument", "m_TermAuthority")
    def validate_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
    
class ChangeRepresentList(BaseModel):
    r_Code: str
    r_Name: str
    r_DocumentSeria: str
    r_DocumentNumber: str
    r_DocumentDate: str
    r_DocumentWho: str
    r_AuthDocument: str
    r_DocumentName: str
    r_TermAuthority: str
    r_Email: str
    r_Phone: str
    r_AuthAuthority: str

    @field_validator(
    "r_Code", "r_Name", "r_DocumentSeria", "r_DocumentNumber", "r_DocumentDate",
    "r_DocumentWho", "r_AuthDocument", "r_DocumentName", "r_TermAuthority", "r_Email",
    "r_Phone", "r_AuthAuthority")
    def validate_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value
    
class ChangeData(BaseModel):
    id: int
    name: str
    documentType: str
    documentDirection: str
    documentStatus: str
    llcMemberType: str
    roleName: str | None
    roleCode: str | None
    outNum: str 
    outDate: str
    isPresentOutNum: bool
    memberAccountReference: str | None
    memberDocumentNumber: str | None
    llcId: int
    clientName: str
    clientFullName: str
    clientCode: str
    memberRoles: str | None
    shareSize: int
    isFullShareSize: bool
    capitalShareAction: str
    counterPartyCode: str 
    counterPartyName: str
    nameBlockFor: str
    codeBlockFor: str
    blockReasonNameOther: str
    capitalShareLLCId: str | None
    escrowAccountNumber: str
    escrowDocumentNumber: str
    escrowDocumentDate: str
    contractNum: str 
    contractDate: str 
    holderBalance: str | None
    accountClass: str | None
    messageCdData: str
    messageCdTopic: str
    messageCdFileUrl: str
    signatures: list
    files: list
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int
    p_Surname: str
    p_Name: str
    p_Secondname: str
    p_Code: str
    p_IsCodeExist: bool
    p_CodeEDDR: str
    p_Citizenship: str
    p_BirthPlace: str
    p_DocumentName: str
    p_DocumentNumber_Series: str
    p_DocumentNumber: str
    p_DocumentDate: str
    p_DocumentWho: str
    p_BirthDate: str
    p_Country: str
    p_Region: str
    p_City: str
    p_Address: str
    p_PostIndex: str
    p_Is_Mailing_Address_Matches_Location: bool
    p_CodeTerUnit: str
    p_TaxResidencyStatusResName: bool
    p_IsFOP: bool
    p_FOPAuthority: str
    p_PostAddress: str
    p_Phone: str
    p_MobilePhone: str
    p_Email: str
    p_ContractNum: str
    p_ContractDate: str
    p_EmailSend: str
    p_BankName: str
    p_BankMFO: str
    p_BankAccount: str
    mg_Name: str
    mg_Code: str
    mg_IsJur: bool
    mg_AuthDocument: str
    mg_TermAuthority: str
    mg_DocumentNumber_Series: str
    mg_DocumentNumber: str
    firstPersonName: str
    firstPersonCode: str
    firstPersonCode_DocumentNumber_Series: str
    firstPersonCode_DocumentNumber: str
    firstPersonPosition: str
    f_DocumentInfo: str
    f_TermAuthority: str
    managerList: list[ChangeManagerList]
    representList: list[ChangeRepresentList]
    jurNonResidentName: str
    jurNonResidentShortName: str
    jurNonResidentCode: str
    jurNonResidentRegCountry: str
    p_TaxResidencyStatusResOwnersName: bool
    jurName: str
    jurShortName: str
    jurShortNameEng: str
    jurEdrpou: str
    jurEdrisi: str
    jurRegCountry: str
    govName: str
    govShortName: str
    govCode: str
    letterDepository: str | None

    @field_validator(
    "id", "name", "documentType", "documentDirection", "documentStatus",
    "llcMemberType", "outNum", "outDate", "isPresentOutNum",
    "llcId", "clientName", "clientFullName", "clientCode" ,"shareSize","isFullShareSize", "capitalShareAction", "counterPartyCode", "counterPartyName",
    "nameBlockFor", "codeBlockFor", "blockReasonNameOther", "escrowAccountNumber", "escrowDocumentNumber", "escrowDocumentDate", "contractNum", "contractDate", "messageCdData","messageCdTopic","messageCdFileUrl", "signatures", "files", "countOfSignaturesForDocument",
    "countOfStampsForDocument", "p_Surname", "p_Name", "p_Secondname", "p_Code", "p_IsCodeExist", "p_CodeEDDR", "p_Citizenship", "p_BirthPlace", "p_DocumentName", "p_DocumentNumber_Series", "p_DocumentNumber", "p_DocumentDate", "p_DocumentWho", "p_BirthDate", "p_Country",
    "p_Region", "p_City", "p_Address", "p_PostIndex", "p_Is_Mailing_Address_Matches_Location", "p_CodeTerUnit", "p_TaxResidencyStatusResName", "p_IsFOP", "p_FOPAuthority", "p_PostAddress", "p_Phone", "p_MobilePhone", "p_Email", "p_ContractNum", "p_ContractDate", "p_EmailSend", "p_BankName", "p_BankMFO", "p_BankAccount",
    "mg_Name", "mg_Code", "mg_IsJur", "mg_AuthDocument", "mg_TermAuthority", "mg_DocumentNumber_Series", "mg_DocumentNumber", "firstPersonName", "firstPersonCode", "firstPersonCode_DocumentNumber_Series", "firstPersonCode_DocumentNumber", "firstPersonPosition",
    "f_DocumentInfo", "f_TermAuthority", "managerList", "representList", "jurNonResidentName", "jurNonResidentShortName", "jurNonResidentCode", "jurNonResidentRegCountry", "p_TaxResidencyStatusResOwnersName", "jurName", "jurShortName", "jurShortNameEng", "jurEdrpou", "jurEdrisi", "jurRegCountry", "govName", "govShortName", "govCode")
    def validate_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value

class ChangeDocumentModel(BaseModel):
    message: int
    innerMessage: str | None
    data: ChangeData

    @field_validator(
    "message", "data")
    def validate_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        return value