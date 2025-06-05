from fastapi import FastAPI
from pydantic import BaseModel

from rag_indexing import index_text_block, get_index_counts, get_index_sample, clear_indexes

app = FastAPI()

@app.get("/api/hello")
async def read_hello():
    return {"message": "Hello from FastAPI!"}


class TextPayload(BaseModel):
    text: str


@app.post("/api/index")
async def index_notes(payload: TextPayload):
    try:
        index_text_block(payload.text)
        counts = get_index_counts()
        sample = get_index_sample()
        return {"status": "success", "counts": counts, "sample": sample}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/clear")
async def clear_index():
    try:
        clear_indexes()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}