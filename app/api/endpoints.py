from fastapi import APIRouter
from app.models.schemas import Query, Answer
from app.main import generator

router = APIRouter()

@router.post("/ask", response_model=Answer)
async def ask_question(query: Query):

    response = generator(query.question, max_length= 100, num_return_sequences= 1)
    return Answer(answer = response[0]['generated_text'])