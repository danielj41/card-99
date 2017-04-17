from game import Player, Game, N_ACE, N_10, DISPLAY_CARD


class HumanPlayer(Player):
    def getName(self):
        return "You"

    def chooseHandIndex(self, discard, score):
        print
        print
        print "YOUR TURN"
        print
        print "Current score:  ", score.getScore()
        print "Top of discard: ", DISPLAY_CARD[discard.top()]
        print
        print "Your hand:"
        print "1 -", DISPLAY_CARD[self.hand[0]]
        print "2 -", DISPLAY_CARD[self.hand[1]]
        print "3 -", DISPLAY_CARD[self.hand[2]]
        print

        choice = None
        while (choice not in (1, 2, 3)):
            choice = int(raw_input("Which card? "))
        index = choice - 1

        print

        option = None
        if (self.hand[index] in (N_ACE, N_10)):
            choice = None
            if (self.hand[index] == N_ACE):
                print "1 - Add 1"
                print "2 - Add 11"
                print
            if (self.hand[index] == N_10):
                print "1 - Subtract 10"
                print "2 - Add 10"
                print
            while (choice not in (1, 2)):
                choice = int(raw_input("Which value? "))
            option = choice - 1

        return index, option

def play(opponent):
    def announce(text):
        print text

    game = Game([opponent, HumanPlayer(2)])

    winner = None

    while (winner is None):
        winner = game.playTurn(announce)

    print winner.getName(), "WINS"

if __name__ == '__main__':
    play(Player(1))
