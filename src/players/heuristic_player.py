import game.card as C
from game.player import Player

import random

class HeuristicPlayer(Player):
    def getName(self):
        return "Heuristic_" + str(self.uniqid)

    def chooseHandIndex(self, discard, score):
        choices = [(0, C.O_SMALL), (1, C.O_SMALL), (2, C.O_SMALL), (0, C.O_LARGE), (1, C.O_LARGE), (2, C.O_LARGE)]
        random.shuffle(choices)

        handIndex = 0
        option = 0
        wouldLose = True
        while (len(choices) > 0 and wouldLose):
            (handIndex, option) = choices.pop()
            wouldLose = score.wouldCardPlayCauseLoss(self.hand[handIndex], option)

        return handIndex, option
