# Constants and util functions for card values.

# A deck has cards 1-13 in 4 suits.
N_MIN = 1
N_MAX = 13
NUM_SUITS = 4

# A player's hand has 3 cards.
PER_PLAYER = 3

# Names for each card value.
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

# Function for displaying cards to the user.
DISPLAY_CARD = {
    N_ACE: 'Ace',
    N_2: '2',
    N_3: '3',
    N_4: '4',
    N_5: '5',
    N_6: '6',
    N_7: '7',
    N_8: '8',
    N_9: '9',
    N_10: '10',
    N_JACK: 'Jack',
    N_QUEEN: 'Queen',
    N_KING: 'King'
}

def displayTitle(card):
    return DISPLAY_CARD[card]

# These cards can be used to do two different things.
OPTION_CARDS = [N_ACE, N_10]

def isOptionCard(card):
    return card in OPTION_CARDS

# A player's play will include an "option" if they play one of those two cards.
O_SMALL = 0
O_LARGE = 1

# A function for displaying option choices to the user.
DISPLAY_OPTION = {
    N_ACE: {
        O_SMALL: 'Add 1',
        O_LARGE: 'Add 11'
    },
    N_10: {
        O_SMALL: 'Subtract 10',
        O_LARGE: 'Add 10'
    }
}

def optionDisplayTitle(card, option):
    return DISPLAY_OPTION[card][option]
