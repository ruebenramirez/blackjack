

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand = []
        for card in self.cards:
            hand.append(str(card))
        return ' '.join(hand)

    def add_card(self, card):
        '''add card to hand'''
        self.cards.append(card)

    def value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            if card.value == "A":
                # save Ace valuation for last
                ace_count += 1
            elif (card.value == "K"
                    or card.value == "Q"
                    or card.value == "J"):
                value = value + 10
            else:
                value = value + int(card.value)

        # value Aces in the hand last
        for i in range(ace_count):
            high_ace_value = value + 11
            if high_ace_value <= 21:
                value = high_ace_value
            else:
                value = value + 1

        return value

    def bust(self):
        if self.value() > 21:
            return True
        return False
