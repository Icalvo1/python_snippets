## shitty Battleship game
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def grid_clean(num):
    if num == 0:
        return num + 1
    elif num > 0 or num <=5:
        return num - 1
    elif isinstance(num, basestring) or num =='':
        print 'guess must be a number'
    else: 
        return num

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
guess_row = grid_clean(int(raw_input("Guess Row:")))
guess_col = grid_clean(int(raw_input("Guess Col:")))


# Write your code below!

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
elif board[guess_row][guess_col] == 'X':
    print "You guessed that one already."
elif guess_row > range(5) or guess_col > range(5):
    print "Oops, that's not even in the ocean."
else:
    board[guess_row][guess_col] = 'X'
    print "You missed my battleship!"
    print_board(board)
    print grid_clean(ship_row)
    print grid_clean(ship_col)