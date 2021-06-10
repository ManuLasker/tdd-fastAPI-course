from datetime import datetime

from pydantic import AnyHttpUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummarySchema(SummaryResponseSchema):
    summary: str
    created_at: datetime


class SummaryInDBBase(SummarySchema):
    class Config:
        orm_mode = True


class Summary(SummaryInDBBase):
    pass
