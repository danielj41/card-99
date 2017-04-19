from game import Game
from card import N_ACE, N_10, O_SMALL, O_LARGE, cardDisplayTitle, isOptionCard, cardOptionDisplayTitle
from player import Player

class HumanPlayer(Player):
    def getName(self):
        return "You"

    def chooseHandIndex(self, discard, score):
        print
        print
        print "YOUR TURN"
        print
        print "Current score:  ", score.getScore()
        print "Top of discard: ", cardDisplayTitle(discard.top())
        print
        print "Your hand:"
        print "1 -", cardDisplayTitle(self.hand[0])
        print "2 -", cardDisplayTitle(self.hand[1])
        print "3 -", cardDisplayTitle(self.hand[2])
        print

        choice = None
        while (choice not in (1, 2, 3)):
            choice = int(raw_input("Which card? "))
        index = choice - 1

        print

        option = None
        card = self.hand[index]

        if (isOptionCard(card)):
            choice = None
            print "1 -", cardOptionDisplayTitle(card, O_SMALL)
            print "2 -", cardOptionDisplayTitle(card, O_LARGE)
            print
            while (choice not in (1, 2)):
                choice = int(raw_input("Which value? "))
            option = O_SMALL if choice == 1 else O_LARGE

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
