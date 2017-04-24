from game import Game
import game.card as C
from game.player import Player
from heuristic_player import HeuristicPlayer

class HumanPlayer(Player):
    def getName(self):
        return "You"

    def chooseHandIndex(self, discard, score):
        print
        print
        print "YOUR TURN"
        print
        print "Current score:  ", score.getScore()
        print "Top of discard: ", C.displayTitle(discard.top())
        print
        print "Your hand:"
        print "1 -", C.displayTitle(self.hand[0])
        print "2 -", C.displayTitle(self.hand[1])
        print "3 -", C.displayTitle(self.hand[2])
        print

        choice = None
        while (choice not in (1, 2, 3)):
            choice = int(raw_input("Which card? "))
        index = choice - 1

        print

        option = None
        card = self.hand[index]

        if (C.isOptionCard(card)):
            choice = None
            print "1 -", C.optionDisplayTitle(card, C.O_SMALL)
            print "2 -", C.optionDisplayTitle(card, C.O_LARGE)
            print
            while (choice not in (1, 2)):
                choice = int(raw_input("Which value? "))
            option = C.O_SMALL if choice == 1 else C.O_LARGE

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
    play(HeuristicPlayer(1))
