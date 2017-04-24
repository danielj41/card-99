from game import Game
from players.heuristic_player import HeuristicPlayer

game = Game([HeuristicPlayer(1), HeuristicPlayer(2), HeuristicPlayer(3), HeuristicPlayer(4)])

def announce(text):
    print text

winner = None

while (winner is None):
    winner = game.playTurn(announce)

print winner.getName(), "WINS"
