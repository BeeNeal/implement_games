from random import sample

class Dominoes(object):
    """"""
# Intialize game with amt players
    def __init__(self, n_players):
        self.n_players = n_players

# Build this game's boneyard
    def build_boneyard(self):
        """Generates (0,0) - (6, 6) tuples representing dominoes"""

        boneyard = set()
        for i in range(7):
            for j in range(7):
                bone = (i, j)
                if (j, i) in boneyard:
                    continue
                else:
                    boneyard.add(bone)
        self.boneyard = boneyard
        return boneyard

# add players to game
    def add_players(self):
        """ """
        players = []
        for p in range(self.n_players):
            name = raw_input("What's your name, player {}?".format(p))
            self.players.append(Player(name))
        return players

def remove_bones_from_boneyard(bones, boneyard):
    """Takes in set of bones, removes these bones from boneyard"""

    boneyard = boneyard - bones
    return boneyard


# def create_player(n_players, boneyard):

#     bones = assign_bones(n_players, boneyard)
#     remove_bones_from_boneyard(bones, boneyard)


class Player(object):

    def __init__(self, name, first=False):
        # self.bones = bones
        self.name = name
        self.first = first

    def assign_bones(self, n_players, boneyard):
        """Assigns bones from boneyard, amount dependent on number of players"""

        amt_to_take = 28/n_players - 1
        personal_bones = set(sample(boneyard, amt_to_take))
        remove_bones_from_boneyard(personal_bones, boneyard)

        self.bones = personal_bones

    def is_first(self):
        if (6, 6) in self.bones:
            self.first = True
        return


game = Dominoes(4)
game.build_boneyard()
game.add_players()

# Running Qs
# How should I connect this specific game with # players to this specific player?
# How do I make sure a function is always called