from fastapi import APIRouter, Body, Depends

from app import model
from app.auth import auth_handler, auth_bearer

router = APIRouter()

posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

users = []

def check_user(data: model.UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False



@router.get("/posts", tags=["posts"], dependencies=[Depends(auth_bearer.JWTBearer())])
async def get_posts() -> dict:
    return { "data": posts }

@router.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@router.post("/posts", tags=["posts"], dependencies=[Depends(auth_bearer.JWTBearer())])
async def add_post(post: model.PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@router.post("/user/signup", tags=["user"])
async def create_user(user: model.UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return auth_handler.sign_jwt(user.email)


@router.post("/user/login", tags=["user"])
async def user_login(user: model.UserLoginSchema = Body(...)):
    if check_user(user):
        return auth_handler.sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }