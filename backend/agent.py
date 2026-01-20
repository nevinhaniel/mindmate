from pydantic_ai import Agent
from models import MoodResponse

agent = Agent(
    model="openai/gpt-3.5-turbo",
    result_type=MoodResponse,
    system_prompt=(
        "You are a calm, empathetic mental health support assistant. "
        "You must NOT provide medical advice or diagnoses. "
        "Identify the user's emotion, summarize their feelings, "
        "and give supportive, practical, non-clinical advice."
    )
)
