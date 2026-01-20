from fastapi import FastAPI, HTTPException
from models import MoodInput
from agent import agent

app = FastAPI(title="MindMate AI")

@app.post("/analyze")
async def analyze_mood(data: MoodInput):
    try:
        result = await agent.run(data.message)
        return result.data
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI processing failed")
