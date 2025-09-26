from enum import Enum


class Card:
    class Color(Enum):
        HEART = 0
        SPADE = 1
        CLUB = 2
        DIAMOND = 3

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{ self.number } of { self.color }"

    def __repr__(self):
        return str(self)


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(Card.Color(i), j + 1))


if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
