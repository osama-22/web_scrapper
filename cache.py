import redis
from config import REDIS_HOST, REDIS_PORT

class Cache:
    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        self.client.set(key, value)

    def delete(self, key):
        self.client.delete(key)
