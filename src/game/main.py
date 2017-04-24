import random

import card as C
from deck import Deck
from discard import DiscardPile
from score import Score

# Represents a single game with a set of players.
class Game:
    # Pass in a list of players.
    def __init__(self, players):
        # Make the players play in a random order.
        self.players = players
        random.shuffle(self.players)

        # Start with the first player, going in the positive direction (some
        # cards can change the direction of play.)
        self.curPlayerIndex = 0
        self.playerDirection = 1

        self.score = Score()

        self.discard = DiscardPile()
        self.deck = Deck(self.discard)

        # Give each player 3 cards from the top of the deck.
        for i in range(C.PER_PLAYER):
            for player in self.players:
                player.draw(self.deck.pop())

    # Plays a single turn. If set, `announce` will be called with a
    # human-readable description of the turn.
    #
    # Returns `None` if the game hasn't ended, and returns a player if that
    # player won.
    def playTurn(self, announce=None):
        # It's this player's turn.
        player = self.players[self.curPlayerIndex]

        # Get their play, add it to the discard pile and have them draw a new
        # card from the deck.
        card, option = player.playCard(self.discard, self.score)
        self.discard.append(card)
        player.draw(self.deck.pop())

        # If the deck has zero cards, reshuffle the discard pile.
        self.deck.recreateIfNeeded(self.discard)

        if (announce):
            announce(player.getName() + " played " + C.displayTitle(card))

        # Update the score.
        self.score.cardPlayed(card, option)

        # If this play caused the player to lose, remove them from the game.
        if (self.score.didPlayerLose()):
            if (announce):
                announce(player.getName() + " is OUT")
            self.score.reset() # Restart score at 0 for remaining players.
            self.removeCurPlayer()

        # If one player is left, they won.
        if (len(self.players) == 1):
            return self.players[0]

        # Figure out whose turn it is next.
        self.setNextPlayer(card)

        # No one won, so return None.
        return None

    # The deletes the current player. Used when they lose.
    def removeCurPlayer(self):
        del self.players[self.curPlayerIndex]

    # Picks the player to take the next turn.
    def setNextPlayer(self, card):
        if (card == C.N_3):
            # 3s skip the next player.
            self.curPlayerIndex += 2 * self.playerDirection
        elif (card == C.N_4):
            # 4s swap the direction of play.
            self.playerDirection = -self.playerDirection
            self.curPlayerIndex += self.playerDirection
        else:
            self.curPlayerIndex += self.playerDirection

        if (len(self.players) > 0):
            self.curPlayerIndex = self.curPlayerIndex % len(self.players)
