from config import MAX_CARD_VALUE

class Card:
    value: int
    literal: str
    suit: str

    def __get_literal_by_value(self, value: int) -> str:
        if value <= 10:
            return str(value)
        name_by_value: dict[int, str] = {
            11: 'Q',
            12: 'J',
            13: 'K'
        }
        return name_by_value.get(value)

    def __init__(self, value: int, suit: str) -> None:
        self.value = min(value, MAX_CARD_VALUE)
        self.suit = suit
        self.literal = self.__get_literal_by_value(value)
    

    def to_str(self) -> str:
        return f'{self.literal} {self.suit} (Value: {self.value})'
        
        