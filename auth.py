from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from config import API_KEY

api_key_header = APIKeyHeader(name="Authorization")

def get_current_user(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return "authorized_user"
