from fastapi import APIRouter
from app.models.schemas import Query, Answer

router = APIRouter()

@router.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    return Answer(answer = "This is a smaple answer.")