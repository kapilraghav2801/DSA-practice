from fastapi import FastAPI, HTTPException
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Todo List API")

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: str

todos = []
todo_id_counter = 1

@app.get("/")
async def root():
    return {
        "message": "Welcome to Todo API",
        "endpoints": ["/todos", "/todos/{todo_id}"]
    }

# HERE: response_model=Todo ensures the response follows this structure
@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    global todo_id_counter

    new_todo = {
        "id": todo_id_counter,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "created_at": datetime.now().isoformat()
    }
    
    todos.append(new_todo)
    todo_id_counter += 1
    
    return new_todo

# HERE: response_model=Todo validates GET response
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# HERE: response_model returns list of Todos
@app.get("/todos", response_model=list[Todo])
async def get_all_todos():
    return todos