
def is_flushdraw(suits):
    return (suits.count(1) == 4 or suits.count(2) == 4 or suits.count(3) == 4 or suits.count(4) == 4)

def is_bdfd(suits):
    return (suits.count(1) == 3 or suits.count(2) == 3 or suits.count(3) == 3 or suits.count(4) == 3)

def is_straight(sorted_card_ranks_array):
    sorted_card_ranks_array = sorted(list(set(sorted_card_ranks_array)))
    chain = 0
    previous = sorted_card_ranks_array[0]
    for ele in sorted_card_ranks_array[1:]:
        if ele == previous + 1:
            chain += 1
            if chain >= 4:
                return True
        else:
            chain = 0
        previous = ele
    return False

def is_oesd(sorted_card_ranks_array):
    sorted_card_ranks_array = sorted(list(set(sorted_card_ranks_array)))
    chain = 0
    previous = sorted_card_ranks_array[0]
    for ele in sorted_card_ranks_array[1:]:
        if ele == previous + 1:
            chain += 1
            if chain >= 3:
                return True
        else:
            chain = 0
        previous = ele
    # Double gutter:
    for i in range(0,len(sorted_card_ranks_array)-4):
        if sorted_card_ranks_array[i] == sorted_card_ranks_array[i+1] - 2 and sorted_card_ranks_array[i] == sorted_card_ranks_array[i+2] - 3 and sorted_card_ranks_array[i] == sorted_card_ranks_array[i+3] - 4 and sorted_card_ranks_array[i] == sorted_card_ranks_array[i+4] - 6:
            return True

    return False

def is_gutshot(sorted_card_ranks_array):
    sorted_card_ranks_array = sorted(list(set(sorted_card_ranks_array)))
    try:
        if sorted_card_ranks_array[3] - sorted_card_ranks_array[0] <= 4 or sorted_card_ranks_array[4] - sorted_card_ranks_array[1] <= 4 or sorted_card_ranks_array[5] - sorted_card_ranks_array[2] <= 4 or sorted_card_ranks_array[6] - sorted_card_ranks_array[3] <= 4:
            return True
    except:
        pass
    return False
