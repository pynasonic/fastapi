from fastapi import APIRouter, Path

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"msg": "todo added successfully."}

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
