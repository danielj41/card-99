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
        choices = [(0, O_SMALL), (1, O_SMALL), (2, O_SMALL), (0, O_LARGE), (1, O_LARGE), (2, O_LARGE)]
        random.shuffle(choices)

        handIndex = 0
        option = 0
        wouldLose = True
        while (len(choices) > 0 and wouldLose):
            (handIndex, option) = choices.pop()
            wouldLose = score.wouldCardPlayCauseLoss(self.hand[handIndex], option)

        return handIndex, option

    def playCard(self, discard, score):
        handIndex, option = self.chooseHandIndex(discard, score)
        card = self.hand[handIndex]
        del self.hand[handIndex]
        return card, option
