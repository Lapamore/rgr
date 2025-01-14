from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    text: str = Field(..., description="Text to summarize")


class SummaryResponse(BaseModel):
    summary: str
