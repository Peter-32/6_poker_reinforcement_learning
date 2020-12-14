
def play_preflop():
    players_remaining = 6
    raises = 0
    while players_remaining != 2:
        players_remaining = 6
        raises = 0
        hands, deck = get_randomized_9_hands()
        raiser_position = None
        opponent_number = 0
        # LJ Turn
        action1 = get_players_first_and_second_and_third_preflop_action(1, raises, raiser_position, hands[0])
        if "r" in action1:
            raises += 1
            raiser_position = 1
        elif action1 == "f":
            players_remaining -= 1
        # HJ Turn
        action2 = get_players_first_and_second_and_third_preflop_action(2, raises, raiser_position, hands[1])
        if "r" in action2:
            raises += 1
            raiser_position = 2
        elif action2 == "f":
            players_remaining -= 1
        # CO Turn
        action3 = get_players_first_and_second_and_third_preflop_action(3, raises, raiser_position, hands[2])
        if "r" in action3:
            raises += 1
            raiser_position = 3
        elif action3 == "f":
            players_remaining -= 1
        # BN Turn
        action4 = get_players_first_and_second_and_third_preflop_action(4, raises, raiser_position, hands[3])
        if "r" in action4:
            raises += 1
            raiser_position = 4
        elif action4 == "f":
            players_remaining -= 1
        # BN Turn
        action5 = get_players_first_and_second_and_third_preflop_action(5, raises, raiser_position, hands[4])
        if "r" in action5:
            raises += 1
            raiser_position = 5
        elif action5 == "f":
            players_remaining -= 1
        # BN Turn
        action6 = get_players_first_and_second_and_third_preflop_action(6, raises, raiser_position, hands[5])
        if "r" in action6:
            raises += 1
            raiser_position = 6
        elif action6 == "f":
            players_remaining -= 1
        preflop_actions = [action1, action2, action3, action4, action5, action6]
        unique_players_with_a_raise = sum([1 for x in preflop_actions if 'r' in x])
        temp = [x for x in preflop_actions if x != 'f']
        if len(temp) != 2:
            players_remaining = 1
            continue
        if unique_players_with_a_raise == 3 and temp[0] == 'rr':
            preflop_actions = [x[0:3] for x in preflop_actions]
        elif unique_players_with_a_raise == 2:
            preflop_actions = [x[0:2] for x in preflop_actions]
        elif unique_players_with_a_raise == 1:
            preflop_actions = [x[0] for x in preflop_actions]
        if len(temp) == 2 and 'f' in temp[0] and temp[1].count('r') >= temp[0].count('r'):
            players_remaining = 1
            continue
    board = deck[0:5]

    hands_remaining = []
    for i, x in enumerate([x != 'f' for x in preflop_actions]):
        if x:
            hands_remaining.append(hands[i])

    range1 = get_range_player_1(preflop_actions)
    range2 = get_range_player_2(preflop_actions)
    return hands_remaining, board, range1, range2

def get_players_first_and_second_and_third_preflop_action(seat_at_the_table, raises, raiser_position, hand):
    first_and_second_action = get_players_first_and_second_preflop_action(seat_at_the_table, raises, raiser_position, hand)
    if first_and_second_action == 'rr':
        if hand in [[14,14], [13,13]]:
            return 'rrr'
        else:
            return 'rrf'
    else:
        return first_and_second_action

def get_players_first_and_second_preflop_action(seat_at_the_table, raises, raiser_position, hand):
    first_action = get_players_first_preflop_action(seat_at_the_table, raises, raiser_position, hand)
    if first_action != 'r':
        return first_action

    h = hand[2]
    suited = hand[3]
    paired = len(set(h)) == 1
    if suited:
        if (h == [14,13]) or (h in [[14,5], [14,4]]):
            return 'rr'
        elif h[1] >= 10:
            return 'rc'
        else:
            return 'rf'
    elif paired:
        if h[0] >= 12:
            return 'rr'
        elif h[0] >= 7:
            return 'rc'
        else:
            return 'rf'
    else:
        if h == [14,13]:
            return 'rr'
        elif (h == [14,12]):
            return 'rc'
        else:
            return 'rf'


def get_players_first_preflop_action(seat_at_the_table, raises, raiser_position, hand):
    h = hand[2]
    suited = hand[3]
    paired = len(set(h)) == 1
    if raises == 0:
        if seat_at_the_table == 1:
            if suited:
                if h[1] >= 9:
                    return 'r'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 5:
                    return 'r'
                else:
                    return 'f'
            else:
                if h in [[14,13], [14,12], [14,11], [13,12]]:
                    return 'r'
                else:
                    return 'f'
        elif seat_at_the_table == 2:
            if suited:
                if h[1] >= 9:
                    return 'r'
                else:
                    return 'f'
            elif paired:
                return 'r'
            else:
                if h[1] >= 11:
                    return 'r'
                else:
                    return 'f'
        elif seat_at_the_table == 3:
            if suited:
                if (h[1] >= 9) or (h[0] == 14 and h[1] >= 5):
                    return 'r'
                else:
                    return 'f'
            elif paired:
                return 'r'
            else:
                if h[1] >= 10:
                    return 'r'
                else:
                    return 'f'
        elif seat_at_the_table == 4:
            if suited:
                if (h[1] >= 8) or (h[0] == 14) or (h[0]-h[1] <= 2 and h[1] != 2):
                    return 'r'
                else:
                    return 'f'
            elif paired:
                return 'r'
            else:
                if h[1] >= 9:
                    return 'r'
                else:
                    return 'f'
        elif seat_at_the_table == 5:
            if suited:
                if (h[1] >= 8) or (h[0] == 14) or (h[0]-h[1] <= 2 and h[1] != 2):
                    return 'r'
                else:
                    return 'f'
            elif paired:
                return 'r'
            else:
                if (h[1] >= 9) or (h[0] == 14 and h[1] >= 5):
                    return 'r'
                else:
                    return 'f'
        elif seat_at_the_table == 6:
            if suited:
                if (h[1] >= 9):
                    return 'r'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 9:
                    return 'r'
                else:
                    return 'f'
            else:
                if (h[1] >= 12):
                    return 'r'
                else:
                    return 'f'
    elif raises == 1:
        if seat_at_the_table == 6 and raiser_position == 1:
            if suited:
                if h in [[14,13], [14,12]]:
                    return 'r'
                elif h[1] >= 9:
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 12:
                    return 'r'
                elif h[0] >= 2:
                    return 'c'
                else:
                    return 'f'
            else:
                if h == [14,13]:
                    return 'r'
                elif h[1] >= 11:
                    return 'c'
                else:
                    return 'f'
        elif seat_at_the_table == 6 and raiser_position == 2:
            if suited:
                if h in [[14,13], [14,12], [14,11], [13,12]]:
                    return 'r'
                elif (h[1] >= 9) or (h[0] == 14 and h[1] >= 5):
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 12:
                    return 'r'
                elif h[0] >= 2:
                    return 'c'
                else:
                    return 'f'
            else:
                if h == [14,13]:
                    return 'r'
                elif h[1] >= 10:
                    return 'c'
                else:
                    return 'f'
        elif seat_at_the_table == 6 and raiser_position == 3:
            if suited:
                if h in [[14,13], [14,12], [14,11], [13,12], [12,11], [11,10]]:
                    return 'r'
                elif (h[1] >= 8) or (h[0] == 14) or (h[0]-h[1] <= 2 and h[1] != 2):
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 11:
                    return 'r'
                elif h[0] >= 2:
                    return 'c'
                else:
                    return 'f'
            else:
                if h == [14,13]:
                    return 'r'
                elif h[1] >= 9:
                    return 'c'
                else:
                    return 'f'
        elif seat_at_the_table == 6 and raiser_position == 4:
            if suited:
                if h[1] >= 10:
                    return 'r'
                elif (h[1] >= 8) or (h[0] == 14) or (h[0]-h[1] <= 2 and h[1] != 2):
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 10:
                    return 'r'
                elif h[0] >= 2:
                    return 'c'
                else:
                    return 'f'
            else:
                if h in [[14,13], [14,12], [13,12]]:
                    return 'r'
                elif (h[1] >= 9) or (h[0] == 14 and h[1] >= 5):
                    return 'c'
                else:
                    return 'f'
        elif seat_at_the_table == 6 and raiser_position == 5:
            if suited:
                if h[1] >= 9:
                    return 'r'
                elif (h[1] >= 4) or (h[0] == 14) or (h[0]-h[1] <= 2):
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 9:
                    return 'r'
                elif h[0] >= 2:
                    return 'c'
                else:
                    return 'f'
            else:
                if h in [[14,13], [14,12], [13,12]]:
                    return 'r'
                elif (h[1] >= 8):
                    return 'c'
                else:
                    return 'f'
        elif seat_at_the_table == 5 and raiser_position == 4:
            if suited:
                if h[1] >= 9:
                    return 'r'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 5:
                    return 'r'
                else:
                    return 'f'
            else:
                if h in [[14,13], [14,12], [14,11], [13,12]]:
                    return 'r'
                else:
                    return 'f'
        else:
            if suited:
                if (h == [14,13]) or (h in [[14,5], [14,4]]):
                    return 'r'
                elif h[1] >= 10:
                    return 'c'
                else:
                    return 'f'
            elif paired:
                if h[0] >= 12:
                    return 'r'
                elif h[0] >= 7:
                    return 'c'
                else:
                    return 'f'
            else:
                if h == [14,13]:
                    return 'r'
                elif (h == [14,12]):
                    return 'c'
                else:
                    return 'f'
    else:
        if h in [[14,14], [13,13]]:
            return 'r'
        else:
            return 'f'



def get_range_player_1(actions):
    if sum(['r' in x for x in actions]) > 1:
        return 12
    elif 'r' in actions[0] and sum(['r' in x for x in actions[1:]]) == 0:
        return 1
    elif 'r' in actions[1] and sum(['r' in x for x in (actions[0:1] + actions[2:])]) == 0:
        return 2
    elif 'r' in actions[2] and sum(['r' in x for x in (actions[0:2] + actions[3:])]) == 0:
        return 3
    elif 'r' in actions[3] and sum(['r' in x for x in (actions[0:3] + actions[4:])]) == 0:
        return 4
    elif 'r' in actions[4] and sum(['r' in x for x in (actions[0:4] + actions[5:])]) == 0:
        return 5
    elif sum(['c' == x or 'rc' == x for x in actions]) == 1:
        return 11
    else:
        return 12

def get_range_player_2(actions):
    if sum(['r' in x for x in actions]) > 1:
        return 12
    elif 'c' == actions[5] and 'r' == actions[0][0]:
        return 6
    elif 'c' == actions[5] and 'r' == actions[1][0]:
        return 7
    elif 'c' == actions[5] and 'r' == actions[2][0]:
        return 8
    elif 'c' == actions[5] and 'r' == actions[3][0]:
        return 9
    elif 'c' == actions[5] and 'r' == actions[4][0]:
        return 10
    elif sum(['c' == x or 'rc' == x for x in actions]) == 1:
        return 11
    else:
        return 12
