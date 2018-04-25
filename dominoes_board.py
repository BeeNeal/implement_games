from dominoes import *

# current options = array[0][0] and array[-1][-1]
# don't actually need LL, because don't need to keep track of bones already used
# only keep track of current_options (this will change when make visual)
e_side = 6
w_side = 6

# north and south only count for scoring when played off of, so start at 0
n_side = 0
s_side = 0

# player plays (4, 6) on left side

w_side = 4

board_score = e_side + w_side + n_side + s_side
if board_score % 5 == 0:
    print "player scored {} points!".format(board_score)



class board(object):

    current_board = []

