import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
RETRY_COUNT = int(os.getenv("RETRY_COUNT", 3))
