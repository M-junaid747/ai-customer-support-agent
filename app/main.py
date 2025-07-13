from fastapi import FastAPI
from app.api.endpoints import router as api_router

app=FastAPI(
    title="AI Customer Support Agent",
    description="API for answering customer queries using a knowledge base.",
    version="0.1.0"
)

@app.get('/health')
async def health_check():
    return { "status":"ok" }


app.include_router(api_router)