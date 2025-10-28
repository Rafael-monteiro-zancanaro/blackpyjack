
from entities.card import Card
from utility import deck_generator


cartas:list[Card] = deck_generator.get_cards_shuffled()


[print(carta.to_str()) for carta in cartas]