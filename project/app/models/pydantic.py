from datetime import datetime

from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    url: str


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
