
def play_flop(strategies, my_position_id, opponent_position_id, hands, deck):
    flop, deck = get_randomized_new_cards(deck=deck, number_of_cards=3)
    return hands, deck, my_winnings_given_postflop, board

def play_turn(strategies, my_position_id, opponent_position_id, hands, deck):
    turn, deck = get_randomized_new_cards(deck=deck, number_of_cards=1)
    return hands, deck, my_winnings_given_postflop, board

def play_river(strategies, my_position_id, opponent_position_id, hands, deck):
    river, deck = get_randomized_new_cards(deck=deck, number_of_cards=1)
    return my_winnings_given_postflop


# This seems worthless, we already have the board from earlier.
def get_randomized_new_cards():
    pass
