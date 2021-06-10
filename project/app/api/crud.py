from typing import List, Optional

from app.models.tortoise import TextSummary

from app.models.pydantic import (  # isort:skip
    Summary,
    SummaryPayloadSchema,
    SummaryUpdatePayloadSchema,
)


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="")
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[Summary]:
    summary = await TextSummary.filter(id=id).first()
    if summary:
        return Summary.from_orm(summary)


async def get_all() -> List[Summary]:
    summaries = await TextSummary.all()
    return [Summary.from_orm(summary) for summary in summaries]


async def delete(id: int) -> int:
    indicator: int = await TextSummary.filter(id=id).first().delete()
    return indicator


async def put(
    id: int, updated_summary: SummaryUpdatePayloadSchema
) -> Optional[Summary]:
    indicator: int = (
        await TextSummary.filter(id=id).first().update(**updated_summary.dict())
    )
    if indicator:
        summary = await TextSummary.filter(id=id).first()
        return Summary.from_orm(summary)
