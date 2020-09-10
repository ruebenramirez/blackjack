from collections import Counter


class Stats:
    def __init__(self):
        self.games = []
        self.player_wins = 0
        self.player_win_percent = 0
        self.win_hands = {}

    def calculate_game_stats(self):
        self.count_player_wins()
        self.calculate_win_percentage()

    def count_player_wins(self):
        win_hand_values = []
        for game in self.games:
            if game.player_won:
                self.player_wins = self.player_wins + 1
                win_hand_values.append(game.winning_hand_value)
        self.win_hands = self.count_win_hand_values(win_hand_values)

    @staticmethod
    def count_win_hand_values(win_hand_values):
        win_hand_values.sort(reverse=True)
        return dict(Counter(win_hand_values).items())

    def calculate_win_percentage(self):
        win_percent = self.player_wins * 100 / len(self.games)
        self.player_win_percent = round(win_percent, 1)

    def print_game_stats(self):
        self.calculate_game_stats()
        print("Number of games: {game_count}\n".format(
            game_count=len(self.games)))
        print("Player Success: {win_percent}%\n".format(
            win_percent=self.player_win_percent))
        print("Player Winning Hand => {win_count} times".format(
            win_count=self.player_wins))
        for hand_value, count in self.win_hands.items():
            print("{value} => {count}".format(value=hand_value, count=count))
