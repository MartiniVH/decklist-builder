from fastapi import APIRouter
from pydantic import BaseModel
from app.dto.card_dto import CardDTO
from app.methods.deck_methods import handle_get_decks, handle_create_decklist
from app.dto.deck_dto import DeckDTO

decks_router = APIRouter()

decks: list[DeckDTO] = [
    DeckDTO(id=0, name="str", essence_types=[], cards=[], created_at="str", updated_at="str", user_id=0),
    DeckDTO(id=1, name="str", essence_types=[], cards=[], created_at="str", updated_at="str", user_id=0),
    DeckDTO(id=2, name="str", essence_types=[], cards=[], created_at="str", updated_at="str", user_id=0),
]


class DecklistBody(BaseModel):
    user_id: int
    commander: CardDTO
    cards: list[CardDTO]


@decks_router.get("/decks/{user_id}", tags=["decks"])
async def get_decks(user_id: int) -> list[DeckDTO]:
    return handle_get_decks(decks, user_id)


@decks_router.post("/decks/decklist/{deck_name}", tags=["decks"])
def create_decklist(deck_name: str, decklist_body: DecklistBody):
    return handle_create_decklist(deck_name, decklist_body.commander, decklist_body.cards, decklist_body.user_id)
