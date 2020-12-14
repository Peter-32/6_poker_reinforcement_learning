import random

def get_randomized_9_hands():
    deck = shuffle_a_deck_of_cards()
    hands, deck = deal_two_cards_to_each(deck)
    return hands, deck

def shuffle_a_deck_of_cards():
    deck = []
    for i in range(2, 15):
        for j in range(1,5):
            deck.append([i, j])
    random.shuffle(deck)
    return deck

def deal_two_cards_to_each(deck):
    """
    hands is 3 elements.  First the two hands including suits.  Then the hand without suits.  Then whether it is suited
    """
    hands = [deck[0:2] + [sorted([deck[0][0], deck[1][0]], reverse=True)] + [deck[0][1] == deck[1][1]],
             deck[2:4] + [sorted([deck[2][0], deck[3][0]], reverse=True)] + [deck[2][1] == deck[3][1]],
             deck[4:6] + [sorted([deck[4][0], deck[5][0]], reverse=True)] + [deck[4][1] == deck[5][1]],
             deck[6:8] + [sorted([deck[6][0], deck[7][0]], reverse=True)] + [deck[6][1] == deck[7][1]],
             deck[8:10] + [sorted([deck[8][0], deck[9][0]], reverse=True)] + [deck[8][1] == deck[9][1]],
             deck[10:12] + [sorted([deck[10][0], deck[11][0]], reverse=True)] + [deck[10][1] == deck[11][1]]]
    deck = deck[12:]
    return hands, deck
