import os 
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
from dotenv import load_dotenv


from pydantic import BaseModel


load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

auth = FastAPI()
basic_auth = HTTPBasic()


class RefreshTokenRequest(BaseModel):
    refresh_token: str



#--------- CREATE ACCESS TOKEN ---------
def create_access(username):
    payload = {
        "sub": username,
        "type" : "access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=5)
    }

    return jwt.encode(
        payload,
        SECRET,
        ALGORITHM
    )
    

# --------- CREATE REFRESH TOKEN ---------
def create_refresh(username):
    payload = {
        "sub": username,
        "type": "refresh",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }

    return jwt.encode(
        payload,
        SECRET,
        algorithm=ALGORITHM
    )


# ------------------ MAIN AUTH ------------------
@auth.post("/login")
def login(
    credentials : HTTPBasicCredentials = Depends(basic_auth)
):
    username = credentials.username 
    password = credentials.password

    if not secrets.compare_digest(username, os.getenv("AUTH_USERNAME")) or not secrets.compare_digest(password, os.getenv("PASSWORD")):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password!!"
        )

    access=create_access(username)
    refresh=create_refresh(username)

    return {
        "access" : access,
        "refresh" : refresh
    }


@auth.post("/refresh")
def refresh(data: RefreshTokenRequest):
    try:
        payload = jwt.decode(
            data.refresh_token,
            SECRET,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=401,
                detail="Invalid token type: refresh token required"
            )

        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=401,
                detail="Invalid token payload"
            )

        new_access_token = create_access(username)

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )