from game import Player, Game, N_ACE, N_10, DISPLAY_CARD

class BadPlayer(Player):
    def getName(self):
        return "Bad_" + str(self.uniqid)

    def chooseHandIndex(self, discard, score):
        return 0, 0
