from typing import Union

from pydantic import BaseModel, field_validator



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
