from card import O_SMALL, O_LARGE

import random

class Player:
    def __init__(self, uniqid):
        self.hand = []
        self.uniqid = uniqid

    def getName(self):
        return "Computer_" + str(self.uniqid)

    def draw(self, card):
        self.hand.append(card)

    def chooseHandIndex(self, discard, score):
        raise NotImplementedError('subclasses must override chooseHandIndex')

    def playCard(self, discard, score):
        handIndex, option = self.chooseHandIndex(discard, score)
        card = self.hand[handIndex]
        del self.hand[handIndex]
        return card, option
