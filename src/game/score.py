from card import *

class Score:
    def __init__(self):
        self.score = 0

    def cardPlayed(self, card, option):
        self.score = self.getNewScore(card, option)
        if (self.score < 0):
            self.score = 0

    def getNewScore(self, card, option):
        if (card == N_ACE):
            if (option == O_SMALL):
                return self.score + 1
            elif (option == O_LARGE):
                return self.score + 11
        elif (card == N_4):
            return self.score
        elif (card == N_9):
            return 99
        elif (card == N_10):
            if (option == O_SMALL):
                return self.score - 10
            elif (option == O_LARGE):
                return self.score + 10
        elif (card == N_JACK or card == N_QUEEN):
            return self.score + 10
        elif (card == N_KING):
            return self.score
        else:
            return self.score + card

    def wouldCardPlayCauseLoss(self, card, option):
        return self.getNewScore(card, option) > 99

    def getScore(self):
        return self.score

    def didPlayerLose(self):
        return self.score > 99

    def reset(self):
        self.score = 0
