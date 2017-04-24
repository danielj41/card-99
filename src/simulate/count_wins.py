from game import Game
from heuristic_player import HeuristicPlayer
from bad_player import BadPlayer

def countWins(numGames, playerTypes):
    wins = {}

    for i in range(numGames):
        players = []
        for i, PlayerType in enumerate(playerTypes):
            players.append(PlayerType(i))

        game = Game(players)

        winner = None
        while (winner is None):
            winner = game.playTurn()

        wins[winner.getName()] = wins.get(winner.getName(), 0) + 1

    print wins

if __name__ == '__main__':
    countWins(10000, [BadPlayer, HeuristicPlayer, HeuristicPlayer])
