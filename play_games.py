from game import Game
from player import Player

game = Game([Player(1), Player(2), Player(3), Player(4)])

def announce(text):
    print text

winner = None

while (winner is None):
    winner = game.playTurn(announce)

print winner.getName(), "WINS"
