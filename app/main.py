from fastapi import FastAPI
from .routers import users, cardgame, decks

app = FastAPI()

# Routers
app.include_router(users.users_router)
app.include_router(cardgame.cardgames_router)

app.include_router(decks.decks_router)

