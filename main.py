from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_client import query_rag

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    message = body.get("message", "")
    reply = query_rag(message)
    return {"reply": reply}
