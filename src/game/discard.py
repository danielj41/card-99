# Represents the cards that players have played.
class DiscardPile:
    def __init__(self):
        self.cards = []

    # Put a card on the discard pile.
    def append(self, card):
        self.cards.append(card)

    # Look at the card at the top of the discard pile.
    def top(self):
        return self.cards[-1]

    # Removes all the cards from the discard pile.
    def takeAll(self):
        cards = self.cards;
        self.cards = []
        return cards

    # Returns how many of a certain card has been played. This is useful for
    # AIs that "count cards."
    def numOfCard(self, card):
        return self.cards.count(card)
