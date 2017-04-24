class DiscardPile:
    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)

    def top(self):
        return self.cards[-1]

    def takeAll(self):
        cards = self.cards;
        self.cards = []
        return cards

    def numOfCard(self, card):
        return self.cards.count(card)
