# Abstract representation of a player of the game. Subclasses must Implements
# the `chooseHandIndex` method.
class Player:
    # uniqueId is just used to give the same type of player a different name.
    def __init__(self, uniqueId):
        self.hand = []
        self.uniqueId = uniqueId

    def getName(self):
        return self.__class__.__name__ + str(self.uniqueId)

    # Adds a new card to the player's hand.
    def draw(self, card):
        self.hand.append(card)

    # Must be overridden by subclasses.
    # Returns (handIndex, option).
    # - handIndex: 0, 1, or 2 to play the card self.hand[handIndex].
    # - option: O_SMALL or O_LARGE for cards that can have two values.
    def chooseHandIndex(self, discard, score):
        raise NotImplementedError('subclasses must override chooseHandIndex')

    # Plays a card, removing it from the player's hand.
    def playCard(self, discard, score):
        handIndex, option = self.chooseHandIndex(discard, score)
        card = self.hand[handIndex]
        del self.hand[handIndex]
        return card, option
