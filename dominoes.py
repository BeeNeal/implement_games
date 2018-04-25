from random import sample

class Dominoes(object):
    """"""
# Intialize game with amt players
    def __init__(self, n_players):
        self.n_players = n_players
        self.boneyard = self.build_boneyard()

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
        self.players = []
        for p in range(self.n_players):
            name = raw_input("What's your name, player {}?".format(p))
            self.players.append(Player(name))
        return self.players


# def create_player(n_players, boneyard):

#     bones = assign_bones(n_players, boneyard)
#     remove_bones_from_boneyard(bones, boneyard)


class Player(object):

    def __init__(self, name):
        # self.bones = bones
        self.name = name
        self.first = False
        self.score = 0

    def remove_bones_from_boneyard(self, bones, boneyard):
        """Takes in set of bones, removes these bones from boneyard"""

        boneyard = boneyard - bones
        return boneyard
        
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
# is there a good way to check if an item is in a list of sets w/o checking all
 # of the<m? - should probably put the 'who starts' method on the game,
 # not the player, and have separate (is_first) on player

# How to construct the actual game
# the board has to be a 2d array, even with excess space

                # [(4, 6)(6, 6)]
# Can have a LL, with pointers to the head and tail! all in the center don't 
# matter once they've been played off of
# player allowed to place at head or tail
        # can have so first elem of first array and last element of array





# Running Qs
# How should I connect this specific game with # players to this set of players?

# Should I build boneyard in the class as method, or have as outside function
#   violates encapsulation 

# if had a DB for this would need tables: GAMES (ID Serialized, boneyard, # players)
# 
# PLAYERS( ID, name)

#ask:
    # how to interact with a different class in a class? eg: need to modify game
    # boneyard from player class's method