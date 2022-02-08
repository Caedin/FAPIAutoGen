from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

service_account_tokens = {
    "centrion-dev" : '789dff9da605d5812b5b884e3e2d20cc9d8baa7c3b91b80d560f08f60b82f8dd'
}

def validate_token(token: str = Depends(oauth2_scheme)):
    if service_account_tokens['centrion-dev'] != token:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return "authenticated"