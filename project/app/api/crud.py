from typing import List, Optional
from app.models.tortoise import TextSummary
from app.models.pydantic import SummaryPayloadSchema, Summary

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url = payload.url,
        summary="dummy summary"
    )
    await summary.save()
    return summary.id

async def get(id: int) -> Optional[Summary]:
    summary = await TextSummary.filter(id=id).first()
    if summary:
        return Summary.from_orm(summary)
    
async def get_all() -> List[Summary]:
    summaries = await TextSummary.all()
    return [Summary.from_orm(summary) for summary in summaries]