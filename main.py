import random


class Gamers:
    file_name = 'gamers.txt'
    players = []

    # read file lines
    # remove all lines with "-" char and remove all whitespaces chars
    def read_file_l(self):
        with open(self.file_name) as file:
            players = file.readlines()

        new_players = []
        for player in players:
            player = player.strip()
            if '-' not in player and player != '':
                new_players.append(player)

        self.players = new_players

    # write players in file
    # add after each player "\n"
    # separate pairs of players by "---...---" sequence
    def write_file_l(self):
        with open(self.file_name, 'w') as file:
            for index, player in enumerate(self.players):
                file.write(player + '\n')
                if index % 2 == 1 and index < len(self.players) - 1:
                    file.write('-' * 10 + '\n')

    def shuffle_players(self):
        random.shuffle(self.players)

    def shift_players(self):
        self.players.insert(0, self.players.pop())


def first_run():
    players = Gamers()
    players.read_file_l()
    players.shuffle_players()
    players.write_file_l()


def other_runs():
    players = Gamers()
    players.read_file_l()
    players.shift_players()
    players.write_file_l()


first_run()
other_runs()
