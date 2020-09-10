import random

from customexceptions import OutOfCardsException
import deck
from hand import Hand


class Shoe:
    """a shoe is composed of one or more decks of cards"""
    def __init__(self, deck_count):
        self.deck_count = deck_count
        self.cards = []
        self.build_shoe()
        self.shuffle()

    def build_shoe(self):
        """build shoe from multiple decks of cards"""
        for i in range(self.deck_count):
            self.cards.extend(deck.build_deck())

    def shuffle(self):
        """shuffle all cards in shoe"""
        random.shuffle(self.cards)

    def deal_hand(self):
        '''deal a hand of two cards'''
        try:
            hand = Hand()
            for i in range(2):
                hand.add_card(self.cards[0])
                self.cards.pop(0)
            return hand
        except IndexError:
            raise OutOfCardsException

    def hit(self, hand):
        '''deal a card for a hit'''
        try:
            hand.add_card(self.cards[0])
            self.cards.pop(0)
        except IndexError:
            raise OutOfCardsException
