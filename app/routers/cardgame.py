from fastapi import APIRouter
from ..methods.cardgame_methods import read_cardgames_method

cardgames_router = APIRouter()


@cardgames_router.get("/cardgame/sets", tags=["cardgame"])
async def read_cardgames():
    return read_cardgames_method()


@cardgames_router.get("/cardgame/sets/1", tags=["cardgame"])
async def read_cardgame():
    return read_cardgames_method()
