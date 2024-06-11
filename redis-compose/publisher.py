from fastapi import FastAPI
from redis import Redis
import uvicorn

app = FastAPI()
redis = Redis(host="redis", port = 6379)

@app.post("/publish")
def publish_messsage(message:str):
    redis.publish("hey", message)
    return {"message" : message}
    