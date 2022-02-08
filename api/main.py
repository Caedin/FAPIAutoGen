from fastapi import Request, FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import SqlManager
import os
import auth
import uvicorn
from pydantic import BaseModel, ValidationError
from utils import auto_mapper
from typing import List

db = SqlManager()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

## ENDPOINTS ##


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("API_PORT")),
        reload=True,
        ssl_keyfile="./server.key",
        ssl_certfile="./server.crt"
    )