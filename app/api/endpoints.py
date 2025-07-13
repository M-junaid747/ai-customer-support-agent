from fastapi import APIRouter
from app.models.schemas import Query, Answer
from app.main import generator
from app.services.knowledge_base import retrieve_context

router = APIRouter()

@router.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    context = retrieve_context(query.question)
    if context:
        prompt = f"Context: {context}\n Question: {query.question}\n Answer: "
    else:
        prompt = query.question

    response = generator(prompt, max_length= 100, num_return_sequences= 1)
    return Answer(answer = response[0]['generated_text'])