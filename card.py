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

def cardDisplayTitle(card):
    return DISPLAY_CARD[card]
