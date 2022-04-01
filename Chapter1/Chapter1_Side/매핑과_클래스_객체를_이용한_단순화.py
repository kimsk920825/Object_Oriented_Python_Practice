class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


def card4(rank, suit):
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(
        rank, NumberCard
    )
    return class_(rank, suit)


if __name__ == "__main__":
    Club, Diamond, Heart, Spade = (
        Suit("Club", "♣"),
        Suit("Diamond", "♦"),
        Suit("Heart", "♥"),
        Suit("Spade", "♠"),
    )
    deck = [
        card4(rank, suit)
        for rank in range(1, 14)
        for suit in (Club, Diamond, Heart, Spade)
    ]

    for object in deck:
        print(object.rank, object.suit)
