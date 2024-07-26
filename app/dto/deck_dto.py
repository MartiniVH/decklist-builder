from typing import List
from pydantic import BaseModel
from app.dto.card_dto import CardDTO


class DeckDTO(BaseModel):
    id: int
    name: str
    essence_types: List[str]
    cards: List[CardDTO]
    created_at: str
    updated_at: str
    user_id: int

