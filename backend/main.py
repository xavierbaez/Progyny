from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Progyny AI Care Guide API")

class AskRequest(BaseModel):
    question: str

@app.get("/")
def health():
    return {"status": "ok", "message": "Progyny FastAPI backend is running"}

@app.post("/ask")
def ask_care_guide(request: AskRequest):
    return {
        "title": "Care Guide Response",
        "summary": f"You asked: {request.question}",
        "suggestions": [
            "Review your Progyny benefit coverage.",
            "Ask whether prior authorization is required.",
            "Confirm which providers are in-network.",
            "Contact your care advocate before making final decisions."
        ],
        "disclaimer": "Educational guidance only. Confirm medical and coverage decisions with your care team."
    }