import random

from card import N_ACE, N_KING

class Deck:
    def __init__(self):
        self.cards = range(N_ACE, N_KING + 1) * 4
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def recreateIfNeeded(self, discard):
        if (len(self.cards) == 0):
            self.cards = discard.takeAll()
            random.shuffle(self.cards)
            discard.append(self.pop())
