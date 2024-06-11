import redis

def subscribing():
    r = redis.Redis(host="redis", port = 6379)
    pubsub = r.pubsub()
    pubsub.subscribe("hey")
    while True:
        for message in pubsub.listen():
            if message['type'] == 'message':
                print(f"Received message: {message['data'].decode('utf-8')}")

subscribing()
