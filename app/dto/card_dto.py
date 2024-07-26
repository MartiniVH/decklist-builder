from typing import List
from enum import Enum
from pydantic import BaseModel


class CardType(str, Enum):
    CREATURE = "Creature",
    ARTIFACT = "Artifact",
    ESSENCE = "Essence",


class CardSubType(str, Enum):
    HUMAN = "Human",
    FEY = "Fey",
    LEGENDARY = "Legendary"


class CardDTO(BaseModel):
    id: int
    name: str
    card_type: List[CardType]
    card_subtype: List[CardSubType]
    is_legendary: bool
    image_small: str
    image_medium: str
    image_large: str
    cost: List[str]
    release_date: str
    amount: int
