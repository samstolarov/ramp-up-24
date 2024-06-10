from fastapi import FastAPI
from redis import Redis

app = FastAPI()
redis = Redis(host="localhost", port = 8090)

@app.post("/publish")
async def publish_messsage(message:str):
    redis.publish("hey", message)
    return {"message" : message}
    