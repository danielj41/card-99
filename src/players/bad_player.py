from game import Game
from card import N_ACE, N_10, DISPLAY_CARD
from player import Player

class BadPlayer(Player):
    def getName(self):
        return "Bad_" + str(self.uniqid)

    def chooseHandIndex(self, discard, score):
        return 0, 0
