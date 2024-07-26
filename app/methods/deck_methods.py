from ..dto.card_dto import CardDTO
from typing import List, TextIO
import os
from ..dto.deck_dto import DeckDTO


def handle_deck_sorting(file: TextIO, commander: CardDTO, cards: List[CardDTO]):
    cards_by_type = dict()

    file.write('[COMMANDER]\n')
    file.write(f'1x - {commander.name}\n\n')
    file.write('\n')

    for card in cards:
        for card_type in card.card_type:
            if card_type not in cards_by_type:
                cards_by_type[card_type] = list()
            cards_by_type[card_type].append(card)

    for card_type in cards_by_type:
        file.write(f'[{card_type.upper()}]\n\n')
        for card_by_type in cards_by_type[card_type]:
            file.write(f'{card_by_type.amount}x - {card_by_type.name}\n')
        file.write('\n\n')


def handle_create_decklist(name: str, commander: CardDTO, cards: List[CardDTO], user_id: int):
    file_path = f"app/files/decklist-{name}-{user_id}.txt"

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w') as file:
        handle_deck_sorting(file, commander, cards)
        return {"message": "File written successfully"}


def handle_get_decks(decks, user_id: int):
    def check_user_id(deck: DeckDTO):
        if deck.user_id == user_id:
            return deck

    filtered_decks: list[DeckDTO] = list(filter(check_user_id, decks))
    return filtered_decks
