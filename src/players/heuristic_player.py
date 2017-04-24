from game import Game
from card import N_ACE, N_10, DISPLAY_CARD, O_SMALL, O_LARGE
from player import Player
import random

class HeuristicPlayer(Player):
    def getName(self):
        return "Heuristic_" + str(self.uniqid)

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
