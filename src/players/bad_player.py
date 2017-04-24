from game.player import Player

class BadPlayer(Player):
    def chooseHandIndex(self, discard, score):
        return 0, 0
