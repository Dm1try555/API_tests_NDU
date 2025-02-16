from typing import Optional, Union
from pydantic import BaseModel, field_validator



class CsvModel(BaseModel):
    ctnreG_CODE: str
    ctnreG_DESC: str

    @field_validator("ctnreG_CODE", "ctnreG_DESC")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CsvByFilterModel(BaseModel):
    ctnreG_CODE: str
    ctnreG_DESC: str

    @field_validator("ctnreG_CODE", "ctnreG_DESC")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


