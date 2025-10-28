from config import SUITS
from entities.card import Card
import pytest
from utility import shuffle


def test_all_suits_have_all_cards() -> None:
    cards: list[Card] = shuffle.get_cards_shuffled()
    (club_cards, diamond_cards, heart_cards, sword_cards) = (0,0,0,0)

    for card in cards:
        match card.suit: 
            case "♥": heart_cards += 1
            case "♦": diamond_cards += 1
            case "♣": club_cards += 1
            case "♠": sword_cards += 1
            case _: pytest.fail('Should have only suitable cards')

    assert club_cards == 13
    assert diamond_cards == 13
    assert heart_cards == 13
    assert sword_cards == 13
    