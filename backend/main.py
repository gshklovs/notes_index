from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
async def read_hello():
    return {"message": "Hello from FastAPI!"}
