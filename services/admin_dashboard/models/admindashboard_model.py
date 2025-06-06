from pydantic import BaseModel, field_validator


class GetAdminDashboardModel(BaseModel):
    totalUsersCount: int
    activeUsersCount: int
    sentDocumentsCountLastWeek: int
    sentDocumentsCountTotal: int
    totalSizeOfFiles: int

    @field_validator("totalUsersCount", "activeUsersCount", "sentDocumentsCountLastWeek", "sentDocumentsCountTotal", "totalSizeOfFiles")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
