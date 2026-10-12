from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from db_conn import MyTable, getsession


app = FastAPI()


# ------------------------ BASIC AUTH ------------------------
security = HTTPBasic()
@app.get("/dataa")
def get_data(
    creds : HTTPBasicCredentials = Depends(security)
):
    username = creds.username
    password = creds.password

    if secrets.compare_digest(username, "pranit") and secrets.compare_digest(password, "hehe"):
        return {"Message" : "Authorized"}
    else:
        return {"Message" : "unauthorized!!"}



# ------------------------ API-KEY ------------------------
API_KEY = "abc-123-xyz"
@app.get("/api")
def get_api(
    api_ : str = Header(...,alias="api_")
):
    if secrets.compare_digest(API_KEY,api_):
        return {"Message" : "Yes sir"}

    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )


# ------------------------ JWT ACCESS & REFRESH TOKENS ------------------------ 
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import secrets


app = FastAPI()


# JWT configuration
SECRET_KEY = "change-this-in-production"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7


# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Tells FastAPI where the client gets its access token
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# Fake database for learning
users = {
    "pranit": {
        "username": "pranit",
        "password_hash": pwd_context.hash("12345")
    }
}


# Refresh-token storage
# Production: Redis or database
refresh_tokens = {}


# --------------------------------------------------
# CREATE ACCESS TOKEN
# --------------------------------------------------

def create_access_token(username: str):

    expire_time = (
        datetime.now(timezone.utc)
        + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    payload = {
        "sub": username,
        "type": "access",
        "exp": expire_time
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# --------------------------------------------------
# CREATE REFRESH TOKEN
# --------------------------------------------------

def create_refresh_token(username: str):

    token = secrets.token_urlsafe(64)

    refresh_tokens[token] = {
        "username": username,
        "expires_at": (
            datetime.now(timezone.utc)
            + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        )
    }

    return token


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    user = users.get(form_data.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    password_correct = pwd_context.verify(
        form_data.password,
        user["password_hash"]
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        user["username"]
    )

    refresh_token = create_refresh_token(
        user["username"]
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# --------------------------------------------------
# VERIFY ACCESS TOKEN
# --------------------------------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "access":
            raise HTTPException(
                status_code=401,
                detail="Invalid token type"
            )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token"
        )


# --------------------------------------------------
# PROTECTED API
# --------------------------------------------------

@app.get("/data")
def get_data(
    username: str = Depends(get_current_user)
):

    return {
        "message": "Authorized",
        "user": username
    }


# --------------------------------------------------
# REFRESH ACCESS TOKEN
# --------------------------------------------------

@app.post("/refresh")
def refresh_access_token(
    refresh_token: str
):

    token_data = refresh_tokens.get(refresh_token)

    if not token_data:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if token_data["expires_at"] < datetime.now(timezone.utc):

        del refresh_tokens[refresh_token]

        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )

    username = token_data["username"]

    # Rotate refresh token
    del refresh_tokens[refresh_token]

    new_access_token = create_access_token(username)

    new_refresh_token = create_refresh_token(username)

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }