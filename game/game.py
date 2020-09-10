from player import Player, Dealer


class Game:
    def __init__(self, shoe):
        self.shoe = shoe
        self.player_one = Player()
        self.dealer = Dealer()

        # used for game stats
        self.player_won = False
        self.winning_hand_value = None

    def play(self):
        self.deal()
        self.turn(self.player_one)
        self.turn(self.dealer)
        self.print_game_result()

    def deal(self):
        '''Deal cards to players'''
        self.player_one.hand = self.shoe.deal_hand()
        self.dealer.hand = self.shoe.deal_hand()

    def turn(self, player):
        '''player one turn'''
        while player.hit() and not player.hand.bust():
            self.shoe.hit(player.hand)

        if not player.hand.bust():
            self.winning_hand_value = player.hand.value()

    def print_game_result(self):
        self.print_hands()
        result = self.determine_game_result()
        if result == "Player" or result == "Dealer":
            print("Result: {winner} wins!\n".format(winner=result))
        else:
            print("Result: Push!\n")

    def print_hands(self):
        print("Player hand: {hand} = {value}".format(
            hand=self.player_one.hand,
            value=self.player_one.hand.value()))
        print("Dealer hand: {hand} = {value}".format(
            hand=self.dealer.hand,
            value=self.dealer.hand.value()))

    def determine_game_result(self):
        '''Who won?'''
        # Did anyone bust?
        if self.player_one.hand.bust():
            self.player_won = False
            return "Dealer"
        elif self.dealer.hand.bust():
            self.player_won = True
            return "Player"

        # Compare hand values
        if self.player_one.hand.value() == self.dealer.hand.value():
            self.player_won = False
            return "Push"
        elif self.player_one.hand.value() < self.dealer.hand.value():
            self.player_won = False
            return "Dealer"
        else:
            self.player_won = True
            return "Player"
