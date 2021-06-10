from typing import List

from app.api import crud
from app.summarizer import generate_summary
from fastapi import APIRouter, BackgroundTasks, HTTPException, Path

from app.models.pydantic import (  # isort:skip
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummarySchema,
    SummaryUpdatePayloadSchema,
)

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema, background_tasks: BackgroundTasks
) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)
    background_tasks.add_task(generate_summary, summary_id, payload.url)
    response_object = {"id": summary_id, "url": payload.url}

    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int = Path(..., gt=0)) -> SummarySchema:
    summary = await crud.get(id)
    if summary:
        return summary
    raise HTTPException(status_code=404, detail="Summary not found")


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


@router.delete("/{id}/", response_model=SummaryResponseSchema)
async def delete_summary(id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary = await crud.get(id)
    if summary:
        await crud.delete(id)
        return summary
    raise HTTPException(status_code=404, detail="Summary not found")


@router.put("/{id}/", response_model=SummarySchema)
async def update_summary(
    update_summary: SummaryUpdatePayloadSchema, id: int = Path(..., gt=0)
) -> SummarySchema:
    summary = await crud.put(id, updated_summary=update_summary)
    if summary:
        return summary
    raise HTTPException(status_code=404, detail="Summary not found")
