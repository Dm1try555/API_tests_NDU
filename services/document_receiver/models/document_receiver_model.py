from typing import Optional, Union
from pydantic import BaseModel, field_validator



class RejectionLetterModel(BaseModel):
    message: str
    data: str

    @field_validator("message", "data")
    def fields_are_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

