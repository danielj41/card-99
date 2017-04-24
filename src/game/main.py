import random

import card as C
from deck import Deck
from discard import DiscardPile
from score import Score

class Game:
    def __init__(self, players):
        self.players = players
        random.shuffle(self.players)
        self.curPlayerIndex = 0
        self.playerDirection = 1

        self.score = Score()
        self.deck = Deck()
        self.discard = DiscardPile()

        for i in range(C.PER_PLAYER):
            for player in self.players:
                player.draw(self.deck.pop())

        self.discard.append(self.deck.pop())

    def playTurn(self, announce=None):
        player = self.players[self.curPlayerIndex]

        card, option = player.playCard(self.discard, self.score)
        self.discard.append(card)
        player.draw(self.deck.pop())

        self.deck.recreateIfNeeded(self.discard)

        if (announce):
            announce(player.getName() + " played " + C.displayTitle(card))

        self.score.cardPlayed(card, option)

        if (self.score.didPlayerLose()):
            if (announce):
                announce(player.getName() + " is OUT")
            self.score.reset()
            self.removeCurPlayer()

        if (len(self.players) == 1):
            return self.players[0]

        self.setNextPlayer(card)

        return None

    def removeCurPlayer(self):
        del self.players[self.curPlayerIndex]
        self.curPlayerIndex -= 1

    def setNextPlayer(self, card):
        if (card == C.N_3):
            self.curPlayerIndex += 2 * self.playerDirection
        elif (card == C.N_4):
            self.playerDirection = -self.playerDirection
            self.curPlayerIndex += self.playerDirection
        else:
            self.curPlayerIndex += self.playerDirection

        if (len(self.players) > 0):
            self.curPlayerIndex = self.curPlayerIndex % len(self.players)
