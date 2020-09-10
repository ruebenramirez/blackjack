import unittest

from player import Player
from card import Card


class TestPlayer(unittest.TestCase):

    def test_player_21_value(self):
        player = Player()
        player.hand.cards = [Card('Spades', 'A'), Card('Clubs', 'K')]
        expected_hand_value = 21
        self.assertEqual(expected_hand_value, player.hand.value())

    def test_player_20_value(self):
        player = Player()
        player.hand.cards = [Card('Spades', 'K'), Card('Clubs', 'K')]
        expected_hand_value = 20
        self.assertEqual(expected_hand_value, player.hand.value())

    def test_player_16_value(self):
        player = Player()
        player.hand.cards = [Card('Spades', 'A'), Card('Clubs', '5')]
        expected_hand_value = 16
        self.assertEqual(expected_hand_value, player.hand.value())

    def test_player_value_of_multiple_aces(self):
        player = Player()
        player.hand.cards = [Card('Spades', 'A'),
                             Card('Spades', 'A'),
                             Card('Spades', 'A'),
                             Card('Spades', 'A'),
                             Card('Clubs', '2'),
                             Card('Clubs', 'Q')]
        expected_hand_value = 16
        self.assertEqual(expected_hand_value, player.hand.value())

    def test_player_stays_at_16(self):
        '''test player turn strategy to stay at 16'''
        # TODO: we need to create a mock for blackjack and pass that into the
        # player during construction
        player = Player()
        # TODO: deal player a hand
        # implementation of dealing the hand: blackjack object should give the
        #    player the cards
        player.hand = [{'suite': 'Spades', 'value': 'A'},
                       {'suite': 'Clubs', 'value': '5'}]
        # TODO: test player's turn strategy to see if they hit at 15
        # player.turn() should call out to blackjack to hit

        pass

    def test_player_hits_at_15(self):
        '''test player turn strategy to hit at 15'''
        pass
