from fastapi import APIRouter
from ..methods.user_methods import read_user_method, read_user_me_method, read_users_method

users_router = APIRouter()


@users_router.get("/users/", tags=["users"])
async def read_users():
    return read_users_method()


@users_router.get("/users/me", tags=["users"])
async def read_user_me():
    return read_user_me_method()


@users_router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return read_user_method(username)
