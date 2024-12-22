#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
import asyncio

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


def get_chat_model():
    model = ChatOllama(model="qwq", temperature=0.7)

    system_prompt = """Organize your response in exactly this format:

    THINKING:
    1. [brief thought]
    2. [brief thought]
    3. [brief thought]
    (maximum 5 steps)

    ANSWER:
    [your final answer]"""

    return model, system_prompt


async def stream_response(message: str):
    model, system_prompt = get_chat_model()
    messages = [SystemMessage(content=system_prompt), HumanMessage(content=message)]

    for chunk in model.stream(messages):
        # Handle smart quotes and other special characters
        content = chunk.content.replace('"', '"').replace('"', '"').replace("'", "'")
        yield content
        await asyncio.sleep(0.01)


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    return StreamingResponse(
        stream_response(request.message),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Transfer-Encoding": "chunked",
            "Content-Type": "text/event-stream; charset=utf-8",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
