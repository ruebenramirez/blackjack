from hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()
        Player.hand_to_beat = 0

    def hit(self):
        '''Does player want another card?'''
        hit = False
        if self.hand.value() < 16:
            hit = True
        if self.hand.value() > Player.hand_to_beat:
            Player.hand_to_beat = self.hand.value()
        return hit


class Dealer(Player):
    def hit(self):
        '''Does Dealer want another card?'''
        if self.hand.value() < Player.hand_to_beat \
                and Player.hand_to_beat <= 21:
            return True
        return False
