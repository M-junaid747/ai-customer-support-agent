from fastapi import FastAPI
from app.api.endpoints import router as api_router
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app=FastAPI(
    title="AI Customer Support Agent",
    description="API for answering customer queries using a knowledge base.",
    version="0.1.0"
)

@app.get('/health')
async def health_check():
    return { "status":"ok" }


app.include_router(api_router)


model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline("text-generation", model= model, tokenizer = tokenizer)