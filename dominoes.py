
class Dominoes(object):

    def build_boneyard():
        """Generates (0,0) - (6, 6) tuples representing dominoes"""

        boneyard = set()
        for i in range(7):
            for j in range(7):
                bone = (i, j)
                if (j, i) in boneyard:
                    continue
                else:
                    boneyard.add(bone)
        return boneyard

class Player():

    personal_bones = 