from pydantic import BaseModel, field_validator


'''Create File'''

class CreateFileData(BaseModel):
    fileName: str
    contentType: str
    fileSize: str
    url: str
    @field_validator("fileName", "contentType", "fileSize", "url")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class CreateFileModel(BaseModel):
    message: str
    data: CreateFileData
    @field_validator("message", "data")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

class CheckFileAfterDeleteModel(BaseModel):
    type: str
    title: str
    status: int
    traceId: str
    @field_validator("type", "title", "status", "traceId")
    def message_is_valid(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
