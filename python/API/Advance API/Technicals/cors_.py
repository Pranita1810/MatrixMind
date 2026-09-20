# -- CROSS ORIGIN RELATION SHARING --
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Define Frontend origins
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get("/cors")
@app.get("/data")
def get_another_origin():
    return {"message": "Hello from FastAPI"}
