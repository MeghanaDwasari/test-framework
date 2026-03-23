import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
API_TIMEOUT = int(os.getenv("API_TIMEOUT", 10))