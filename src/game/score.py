import card as C

# Keeps track of the game's communal "score."
class Score:
    def __init__(self):
        self.score = 0

    # On the "card played" event, add the card's value to the score.
    def cardPlayed(self, card, option):
        self.score = self.getNewScore(card, option)

        # The score cannot go below 0.
        if (self.score < 0):
            self.score = 0

    # Calculates the new score of the game if a certain card is played. `option`
    # is used for cards that can have more than one value.
    def getNewScore(self, card, option):
        # These are defined according to the rules of the game:
        #  - Ace is +1 or +11
        #  - 4 is a +0
        #  - 9 sets the score to 99
        #  - 10 can be +10 or -10
        #  - Jacks and Queens are +10
        #  - Kings are +0
        #  - All other cards add their face value
        if (card == C.N_ACE):
            if (option == C.O_SMALL):
                return self.score + 1
            elif (option == C.O_LARGE):
                return self.score + 11
        elif (card == C.N_4):
            return self.score
        elif (card == C.N_9):
            return 99
        elif (card == C.N_10):
            if (option == C.O_SMALL):
                return self.score - 10
            elif (option == C.O_LARGE):
                return self.score + 10
        elif (card == C.N_JACK or card == C.N_QUEEN):
            return self.score + 10
        elif (card == C.N_KING):
            return self.score
        else:
            return self.score + card

    # Returns `True` if playing a certain card would cause the player to lose.
    def wouldCardPlayCauseLoss(self, card, option):
        return self.getNewScore(card, option) > 99

    def getScore(self):
        return self.score

    # Returns `True` if the last play caused the player to be out.
    def didPlayerLose(self):
        return self.score > 99

    def reset(self):
        self.score = 0
