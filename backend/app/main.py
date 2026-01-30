"""电商客服系统 - FastAPI 入口"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="电商客服系统", version="0.1.0")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "电商客服系统 API"}

@app.post("/api/chat")
async def chat(message: str):
    # TODO: 接入 DeepSeek
    return {"reply": f"收到消息: {message}"}
