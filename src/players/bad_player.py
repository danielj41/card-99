from game.player import Player

class BadPlayer(Player):
    def getName(self):
        return "Bad_" + str(self.uniqid)

    def chooseHandIndex(self, discard, score):
        return 0, 0
