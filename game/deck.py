from card import Card


def build_deck():
    suites = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    card_values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = []
    for s in suites:
        for v in card_values:
            deck.append(Card(s, v))
    return deck
