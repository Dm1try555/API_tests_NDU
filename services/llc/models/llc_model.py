from pydantic import BaseModel, field_validator



'''Get all LLCs by filter'''
class Roles(BaseModel):
    code: str 
    name: str

    @field_validator("code", "name") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class Contracts(BaseModel):
    contacT_TYPE: str 
    cnT_NAME_SURNAME: str
    cnT_NAME_ID_CODE: str
    contacT_START: str
    contacT_END: str | None
    contacT_FIELD_TEXT03: str | None
    cnT_NAME_PASSPORT_NUMBER: str | None
    contacT_FIELD_DATE01: str | None
    telE_NUMBER_MOBILE: str | None
    emaiL_ADDRESS: str | None

    @field_validator("contacT_TYPE", "cnT_NAME_SURNAME", "cnT_NAME_ID_CODE", "contacT_START") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
    

class Members(BaseModel):
    roles: list[Roles] 
    contracts: list[Contracts]
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
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int

    @field_validator("roles", "contracts", "holderBalance", "llcMemberType", "llcMemberTypeName", "accountClass", 
                    "accountReference", "accountCategory", "accountOwnerList", "nameSurname",
                    "nameIdCode", "countOfSignaturesForDocument", "countOfStampsForDocument") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
class LlcItem(BaseModel):
    id: int
    name: str 
    fullName: str
    edrpou: str
    members: list[Members]

    @field_validator("id", "name", "fullName", "edrpou", "members") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcData(BaseModel):
    totalCount: int
    totalNotSendDocumentsCount: int
    items: list[LlcItem]

    @field_validator("totalCount", "items", "totalNotSendDocumentsCount")
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


'''Get LLC by ID'''

class Data(BaseModel):
    id: int
    name: str
    fullName: str
    edrpou: str
    members: list


    @field_validator("id", "name", "fullName", "edrpou", "members")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcIdModel(BaseModel):
    message: str
    data: Data
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value



        

'''Get my LLC'''

class Roles(BaseModel):
    code: str 
    name: str

    @field_validator("code", "name") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class Contracts(BaseModel):
    contacT_TYPE: str 
    cnT_NAME_SURNAME: str
    cnT_NAME_ID_CODE: str
    contacT_START: str
    contacT_END: str
    contacT_FIELD_TEXT03: str
    cnT_NAME_PASSPORT_NUMBER: str
    contacT_FIELD_DATE01: str
    telE_NUMBER_MOBILE: str
    emaiL_ADDRESS: str | None

    @field_validator("contacT_TYPE", "cnT_NAME_SURNAME", "cnT_NAME_ID_CODE", "contacT_START", "contacT_END", "contacT_FIELD_TEXT03", 
                    "cnT_NAME_PASSPORT_NUMBER", "contacT_FIELD_DATE01", "telE_NUMBER_MOBILE") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
    

class Members(BaseModel):
    roles: list[Roles] 
    contracts: list[Contracts]
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
    countOfSignaturesForDocument: int
    countOfStampsForDocument: int

    @field_validator("roles", "contracts", "holderBalance", "llcMemberType", "llcMemberTypeName", "accountClass", 
                    "accountReference", "accountCategory", "accountOwnerList", "nameSurname",
                    "nameIdCode", "countOfSignaturesForDocument", "countOfStampsForDocument") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
class Data(BaseModel):
    id: int
    name: str 
    fullName: str
    edrpou: str
    members: list[Members]

    @field_validator("id", "name", "fullName", "edrpou", "members") 
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class MyLLCModel(BaseModel):
    message: str
    data: list[Data]
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


'''Get LLC Search'''
class SearchItems(BaseModel):
    id: int
    name: str
    fullName: str
    edrpou: str
    
    @field_validator("id", "name", "fullName", "edrpou")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
        
class SearchData(BaseModel):
    totalCount: int
    totalNotSendDocumentsCount: int
    items: list[SearchItems]
    
    @field_validator("totalCount", "totalNotSendDocumentsCount", "items")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class LlcSearchModel(BaseModel):
    message: str
    data: SearchData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value