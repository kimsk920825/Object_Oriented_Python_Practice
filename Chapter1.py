class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    insure = True

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


def card(rank, suit):
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")


if __name__ == "__main__":
    Club, Diamond, Heart, Spade = (
        Suit("Club", "♣"),
        Suit("Diamond", "♦"),
        Suit("Heart", "♥"),
        Suit("Spade", "♠"),
    )
    deck = [
        card(rank, suit)
        for rank in range(1, 14)
        for suit in (Club, Diamond, Heart, Spade)
    ]
    print(dir(deck))
