from curses.ascii import SP


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


class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, "A"),
            11: (FaceCard, "J"),
            12: (FaceCard, "Q"),
            13: (FaceCard, "K"),
        }.get(rank, (NumberCard, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


if __name__ == "__main__":
    Club, Diamond, Heart, Spade = (
        Suit("Club", "♣"),
        Suit("Diamond", "♦"),
        Suit("Heart", "♥"),
        Suit("Spade", "♠"),
    )
    card8 = CardFactory()
    deck8 = [
        card8.rank(r + 1).suit(s)
        for r in range(13)
        for s in (Club, Diamond, Heart, Spade)
    ]

    for object in deck8:
        print(object.rank, object.suit)
