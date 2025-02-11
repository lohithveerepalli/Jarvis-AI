from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import httpx
import json
import asyncio

app = FastAPI()

OLLAMA_API = "http://localhost:11434/api/generate"

class Query(BaseModel):
    prompt: str

async def generate_response(prompt: str):
    """Stream response sentence by sentence for smoother Siri output"""
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", OLLAMA_API, json={"model": "llama3.2:1b", "prompt": prompt, "stream": True}) as response:
            sentence = ""
            async for line in response.aiter_lines():
                if line.strip():
                    try:
                        parsed_line = json.loads(line)
                        sentence += parsed_line["response"]
                        if sentence.endswith((".", "!", "?")):  # Send sentence by sentence
                            yield json.dumps({"response": sentence}) + "\n"
                            sentence = ""  # Reset for next sentence
                    except json.JSONDecodeError:
                        continue

@app.post("/ask")
async def ask(query: Query):
    return StreamingResponse(generate_response(query.prompt), media_type="application/json")
