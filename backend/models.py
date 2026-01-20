from pydantic import BaseModel, Field

class MoodInput(BaseModel):
    message: str = Field(..., min_length=5, max_length=1000)

class MoodResponse(BaseModel):
    emotion: str
    summary: str
    advice: str
