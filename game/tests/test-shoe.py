import unittest

from shoe import Shoe


class TestOneDeckShoe(unittest.TestCase):

    def setUp(self):
        self.shoe = Shoe(1)

    def test_one_deck_card_count(self):
        expected_card_count = 52
        actual_count = len(self.shoe.cards)
        self.assertEqual(expected_card_count, actual_count)

    def test_one_deck_card_uniqueness(self):
        expected_instance_count = 1
        actual_count = len([card for card in self.shoe.cards
                            if card.suite == 'Spades' and card.value == 'A'])
        self.assertEqual(expected_instance_count, actual_count)


class TestSixDeckShoe(unittest.TestCase):

    def setUp(self):
        self.shoe = Shoe(6)

    def test_six_deck_card_count(self):
        expected_card_count = 52 * 6
        actual_count = len(self.shoe.cards)
        self.assertEqual(expected_card_count, actual_count)

    def test_six_deck_card_uniqueness(self):
        expected_instance_count = 6
        actual_count = len([card for card in self.shoe.cards
                            if card.suite == 'Spades' and card.value == 'A'])
        self.assertEqual(expected_instance_count, actual_count)
