import random

import card as C

# Represents the cards that players have not drawn yet.
class Deck:
    # Create and shuffle a new deck.
    def __init__(self, discard):
        self.cards = range(C.N_MIN, C.N_MAX + 1) * C.NUM_SUITS
        random.shuffle(self.cards)
        # Put one card on the discard pile to start.
        discard.append(self.pop())

    # Take one card from the deck.
    def pop(self):
        return self.cards.pop()

    # If the deck is empty, this will recreate itself from the cards in the
    # discard pile.
    def recreateIfNeeded(self, discard):
        if len(self.cards) == 0:
            self.cards = discard.takeAll()
            random.shuffle(self.cards)
            # Put one card back on the discard pile.
            discard.append(self.pop())
