import random

import card as C

class Deck:
    def __init__(self):
        self.cards = range(C.N_MIN, C.N_MAX + 1) * C.NUM_SUITS
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def recreateIfNeeded(self, discard):
        if len(self.cards) == 0:
            self.cards = discard.takeAll()
            random.shuffle(self.cards)
            discard.append(self.pop())
