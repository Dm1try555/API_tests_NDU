from typing import Optional, Union
from pydantic import BaseModel, field_validator


#Get Document Sign 
class GetDocumentSignModel(BaseModel):
    message: str
    data: list

    @field_validator("message", "data")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


