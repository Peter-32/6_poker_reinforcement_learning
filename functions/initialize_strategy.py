import random

def get_randomized_strategies():
    strategies = []
    for i in range(6):
        strategy = get_randomized_strategy()
        strategies.append(strategy)
    return strategies

def get_randomized_strategy():
    strategy = []
    choices = [3, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    length_of_strategy = 40
    for i in range(length_of_strategy):
        strategy.append(random.choices(choices)[0])
    return strategy
