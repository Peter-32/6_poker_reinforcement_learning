import sys
import unittest
from random import seed
sys.path.append('~/Documents/projects/6_poker_reinforcement_learning/functions')
from functions.shuffle_and_deal import *

get_randomized_9_hands

class TestShuffleAndDeal(unittest.TestCase):
    def test_randomized_9_hands(self):
        # Assemble
        seed(32)
        cards_in_a_deck = 52
        players = 6
        cards_dealt = 2
        # Act
        hands, deck = get_randomized_9_hands()
        hands_length = len(hands)
        deck_length = len(deck)
        expected_hands = [[[4, 4], [14, 4], [14, 4], True], [[8, 2], [14, 1], [14, 8], False], [[14, 3],[3, 4], [14, 3], False], [[11, 4], [7, 3], [11, 7], False], [[6, 2], [6, 3], [6, 6], False], [[11, 2], [5, 1], [11, 5], False]]
        expected_deck = [[13, 3], [9, 2], [12, 1], [11,1], [3, 2], [12, 2], [6, 1], [13, 4], [11, 3], [4, 3], [12, 4], [5, 3], [8, 4],[14, 2], [9, 1], [12, 3], [8, 3], [8, 1], [10, 4], [13, 2], [10, 3], [4, 1], [2, 1], [7, 4], [9, 3], [10, 2], [2, 4], [7, 2], [10, 1], [7, 1], [3, 3], [2, 3], [2, 2], [9, 4], [5, 4], [13, 1], [6, 4], [4, 2], [5, 2], [3, 1]]
        expected_hands_length = players
        expected_deck_length = cards_in_a_deck - (players * cards_dealt)
        # Assert
        self.assertEqual(hands, expected_hands)
        self.assertEqual(deck, expected_deck)
        self.assertEqual(hands_length, expected_hands_length)
        self.assertEqual(deck_length, expected_deck_length)

    def test_shuffle_a_deck_of_cards(self):
        # Assemble
        seed(32)
        cards_in_a_deck = 52
        # Act
        deck = shuffle_a_deck_of_cards()
        deck_length = len(deck)
        expected_deck = [[4, 4], [14, 4], [8, 2], [14, 1], [14, 3], [3, 4], [11, 4], [7, 3], [6, 2], [6, 3], [11, 2], [5, 1], [13, 3], [9, 2], [12, 1], [11, 1], [3, 2], [12, 2], [6, 1], [13, 4], [11, 3], [4, 3], [12, 4], [5, 3], [8, 4], [14, 2], [9, 1], [12, 3],[8, 3], [8, 1], [10, 4], [13, 2], [10, 3], [4, 1], [2, 1], [7, 4], [9, 3], [10,2], [2, 4], [7, 2], [10, 1], [7, 1], [3, 3], [2, 3], [2, 2], [9, 4], [5, 4], [13, 1], [6, 4], [4, 2], [5, 2], [3, 1]]
        expected_deck_length = cards_in_a_deck
        # Assert
        self.assertEqual(deck, expected_deck)
        self.assertEqual(deck_length, expected_deck_length)


if __name__ == "__main__":
  unittest.main()
