
from entities.card import Card
from utility import shuffle


cartas:list[Card] = shuffle.get_cards_shuffled()


[print(carta.to_str()) for carta in cartas]