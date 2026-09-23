import jwt
import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv


load_dotenv()


SECRET = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
        

def verify_access_token(
    authorization: str = Header(...)
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Bearer token required"
        )

    token = authorization.split(" ", 1)[1]

    try:
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=401,
                detail="Invalid access token"
            )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Access token expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )