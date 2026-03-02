from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create the app
app = FastAPI(
    title="My First API",
    description="Learning FastAPI from scratch",
    version="1.0.0"
)
user_db = {}
# Global counter for auto-incrementing ID
user_id_counter = 0
#we have to define the request body model
class User(BaseModel):
    id : Optional[int] = None
    name: str
    email: str
    age: int

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to my API",
        "docs_url": "/docs",
        "status": "running"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "my-first-api"
    }

@app.post("/user_create")
async def user_create(user: User):
    global user_id_counter
    user_id_counter += 1
    user.id = user_id_counter
    user_db[user.id] = user
    return {
        "message" : "User create successfully",
        "user": user
    }


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in user_db:
        raise HTTPException(status_code=404, detail = "User not found")
    return user_db[user_id]

