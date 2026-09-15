from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")

@app.get("/")
def home():
    return {"Message" : "Your API is now live"}


@app.get("/user")
def user_info():
    return {"Name" : "Pranit"}


@app.get("/user/data")
async def df():
    return {
        "users":[
            {"id": 1, "name":"Rahul"},
            {"id": 2, "name":"Priyal"},
            {"id": 3, "name":"pranit"},
            {"id": 4, "name":"vasant"},
            {"id": 5, "name":"ugale"}
            ]
            }

# While building new route everytime you have to mention rootpath
# solution : app = FastAPI(root_path="/api/v1") -> mention it here

