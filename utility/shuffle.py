import random
from config import SUITS
from entities.card import Card

def __generate_cards() -> list[Card]:
    return [Card(value, suit) for value in range(1, 14) for suit in SUITS]

def get_cards_shuffled() -> list[Card]:
    cards: list[Card] = __generate_cards()
    random.shuffle(cards)
    return cards


