from typing import Union, List

from pydantic import BaseModel, field_validator, RootModel


class CreateKepVerifyData(BaseModel):
    filled: bool
    issuer: Union[str, None]
    issuerCN: Union[str, None]
    serial: Union[str, None]
    subject: Union[str, None]
    subjCN: Union[str, None]
    subjOrg: Union[str, None]
    subjOrgUnit: Union[str, None]
    subjTitle: Union[str, None]
    subjState: Union[str, None]
    subjLocality: Union[str, None]
    subjFullName: Union[str, None]
    subjAddress: Union[str, None]
    subjPhone: Union[str, None]
    subjEMail: Union[str, None]
    subjDNS: Union[str, None]
    subjEDRPOUCode: Union[str, None]
    subjDRFOCode: Union[str, None]
    timeAvail: bool
    timeStamp: bool
    time: Union[str, None]
    signInfoPtr: Union[str, None]


    @field_validator("filled", "timeAvail", "timeStamp" )
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class KepVerifyModel(BaseModel):
    message: str
    data: CreateKepVerifyData

    @field_validator("message")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetKepGenerateModel(BaseModel):
    token: str
    hash: str

    @field_validator("token", "hash")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetKepIntegrationAccountList(BaseModel):
    ACCOUNT_OWNER_LIST: str
    NAME_SURNAME: str
    NAME_FORENAMES: str #null
    NAME_PATRONYM: str #null
    NAME_ID_CODE: str
    ACCOUNT_REFERENCE: str
    HOLDER_BALANCE: float
    ACCOUNT_CLASS: str
    ACCOUNT_CATEGORY: str

    @field_validator("ACCOUNT_OWNER_LIST", "NAME_SURNAME", "NAME_ID_CODE", "ACCOUNT_REFERENCE",
                     "HOLDER_BALANCE", "ACCOUNT_CLASS", "ACCOUNT_CATEGORY")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetKepIntegrationModel(BaseModel):
    ISSUER_NAME: str
    ISSUER_SHORT_NAME: str
    ISSUER_NUMBER: str
    AccountList: list[GetKepIntegrationAccountList]

    @field_validator("ISSUER_NAME", "ISSUER_SHORT_NAME", "ISSUER_NUMBER")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class GetKepIntegrationListModel(RootModel[List[GetKepIntegrationModel]]):
    pass
