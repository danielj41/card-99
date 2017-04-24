from game import Game
from game.card import N_ACE, N_KING
from heuristic_player import HeuristicPlayer

class LearningPlayer(HeuristicPlayer):
    def __init__(self, uniqid):
        Player.__init__(self, uniqid)
        self.trainingDataInput = []
        self.trainingDataOutput = []

    def getName(self):
        return "Learner"

    def getInputVector(self, discard, score):
        inputVector = []
        inputVector.append(score.getScore() / 99.0)

        for card in self.hand:
            inputCard = [0] * 13
            inputCard[card - 1] = 1
            inputVector += inputCard

        for card in range(N_ACE, N_KING + 1):
            inputVector.append(discard.numOfCard(card) / 4.0)

        return inputVector

    def getChoiceFromOutput(self, output):
        choices = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
        return choices[output]

    def chooseHandIndex(self, discard, score):
        inputVector = self.getInputVector(discard, score)

        handIndex, option = HeuristicPlayer.chooseHandIndex(self, discard, score)

        output = option * 3 + handIndex

        self.trainingDataInput.append(tuple(inputVector))
        self.trainingDataOutput.append(output)

        return handIndex, option

def playGame(numPlayers):
    players = []

    for i in range(numPlayers):
        players.append(LearningPlayer(i + 1))

    game = Game(players)
    winner = None
    while (winner is None):
        winner = game.playTurn()
    return winner.trainingDataInput, winner.trainingDataOutput

def makeTrainingData(numPlays, numPlayers=2):
    trainingDataInput = []
    trainingDataOutput = []

    for i in range(numPlays):
        gameInput, gameOutput = playGame(numPlayers)
        trainingDataInput += gameInput
        trainingDataOutput += gameOutput

    return trainingDataInput, trainingDataOutput

if __name__ == '__main__':
    print makeTrainingData(100)
