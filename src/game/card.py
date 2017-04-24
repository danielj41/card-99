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

N_MIN = 1
N_MAX = 13
NUM_SUITS = 4

PER_PLAYER = 3

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

OPTION_CARDS = [N_ACE, N_10]

O_SMALL = 0
O_LARGE = 1

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

def isOptionCard(card):
    return card in OPTION_CARDS

def optionDisplayTitle(card, option):
    return DISPLAY_OPTION[card][option]
