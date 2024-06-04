from fastapi import FastAPI

app = FastAPI()
@app.get("/{input}")
async def read_name(input : str):
    return {'message' : f"Hello, {input}"}