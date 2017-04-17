import random

N_ACE = 1
N_2 = 2
N_3 = 3
N_4 = 4
N_5 = 5
N_6 = 6
N_7 = 7
N_8 = 8
N_9 = 9
N_10 = 10
N_JACK = 11
N_QUEEN = 12
N_KING = 13

O_SMALL = 0
O_LARGE = 1

DISPLAY_CARD = ['', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Game:
    def __init__(self, players):
        self.players = players
        random.shuffle(self.players)
        self.curPlayerIndex = 0
        self.playerDirection = 1

        self.score = Score()
        self.deck = Deck()
        self.discard = DiscardPile()

        for i in range(3):
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
            announce(player.getName() + " played " + DISPLAY_CARD[card])

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
        if (card == N_3):
            self.curPlayerIndex += 2 * self.playerDirection
        elif (card == N_4):
            self.playerDirection = -self.playerDirection
            self.curPlayerIndex += self.playerDirection
        else:
            self.curPlayerIndex += self.playerDirection

        if (len(self.players) > 0):
            self.curPlayerIndex = self.curPlayerIndex % len(self.players)

class Deck:
    def __init__(self):
        self.cards = range(N_ACE, N_KING + 1) * 4
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def recreateIfNeeded(self, discard):
        if (len(self.cards) == 0):
            self.cards = discard.takeAll()
            random.shuffle(self.cards)
            discard.append(self.pop())

class DiscardPile:
    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)

    def top(self):
        return self.cards[-1]

    def takeAll(self):
        cards = self.cards;
        self.cards = []
        return cards

    def numOfCard(self, card):
        return self.cards.count(card)

class Score:
    def __init__(self):
        self.score = 0

    def cardPlayed(self, card, option):
        self.score = self.getNewScore(card, option)
        if (self.score < 0):
            self.score = 0

    def getNewScore(self, card, option):
        if (card == N_ACE):
            if (option == O_SMALL):
                return self.score + 1
            elif (option == O_LARGE):
                return self.score + 11
        elif (card == N_4):
            return self.score
        elif (card == N_9):
            return 99
        elif (card == N_10):
            if (option == O_SMALL):
                return self.score - 10
            elif (option == O_LARGE):
                return self.score + 10
        elif (card == N_JACK or card == N_QUEEN):
            return self.score + 10
        elif (card == N_KING):
            return self.score
        else:
            return self.score + card

    def wouldCardPlayCauseLoss(self, card, option):
        return self.getNewScore(card, option) > 99

    def getScore(self):
        return self.score

    def didPlayerLose(self):
        return self.score > 99

    def reset(self):
        self.score = 0

class Player:
    def __init__(self, uniqid):
        self.hand = []
        self.uniqid = uniqid

    def getName(self):
        return "Computer_" + str(self.uniqid)

    def draw(self, card):
        self.hand.append(card)

    def chooseHandIndex(self, discard, score):
        choices = [(0, O_SMALL), (1, O_SMALL), (2, O_SMALL), (0, O_LARGE), (1, O_LARGE), (2, O_LARGE)]
        random.shuffle(choices)

        handIndex = 0
        option = 0
        wouldLose = True
        while (len(choices) > 0 and wouldLose):
            (handIndex, option) = choices.pop()
            wouldLose = score.wouldCardPlayCauseLoss(self.hand[handIndex], option)

        return handIndex, option

    def playCard(self, discard, score):
        handIndex, option = self.chooseHandIndex(discard, score)
        card = self.hand[handIndex]
        del self.hand[handIndex]
        return card, option
