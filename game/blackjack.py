from customexceptions import OutOfCardsException
from game import Game
from shoe import Shoe
from stats import Stats


def main():
    decks_of_cards = 6
    shoe = Shoe(decks_of_cards)
    stats = Stats()
    running = True
    while running:
        try:
            game = Game(shoe)
            game.play()
            stats.games.append(game)
        except OutOfCardsException:
            running = False
    stats.print_game_stats()


if __name__ == "__main__":
    main()
