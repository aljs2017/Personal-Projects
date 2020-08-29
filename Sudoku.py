#board_rows = int(input().strip())
#board_columns = int(input().strip())

#for _ in range(board_rows):
#    board.append(list(map(int, input().rstrip().split())))

board = [
    ['5', '3', '.', '.', '7', '.', '1', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '7', '.', '9']
]
def ValidSudoku(board):
    rows = [board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]]
    count = 0

    for a in range(len(board)):
        ones = board[a].count('1')
        if ones > 1:
            return False
        twos = board[a].count('2')
        if twos > 1:
            return False
        threes = board[a].count('3')
        if threes > 1:
            return False
        fours = board[a].count('4')
        if fours > 1:
            return False
        fives = board[a].count('5')
        if fives > 1:
            return False
        sixes = board[a].count('6')
        if sixes > 1:
            return False
        sevens = board[a].count('7')
        if sevens > 1:
            return False
        eights = board[a].count('8')
        if eights > 1:
            return False
        nines = board[a].count('9')
        if nines > 1:
            return False

    for b in range(len(board)):

        ones = board[a].count('1')
        if ones > 1:
            return False
        twos = board[a].count('2')
        if twos > 1:
            return False
        threes = board[a].count('3')
        if threes > 1:
            return False
        fours = board[a].count('4')
        if fours > 1:
            return False
        fives = board[a].count('5')
        if fives > 1:
            return False
        sixes = board[a].count('6')
        if sixes > 1:
            return False
        sevens = board[a].count('7')
        if sevens > 1:
            return False
        eights = board[a].count('8')
        if eights > 1:
            return False
        nines = board[a].count('9')
        if nines > 1:
            return False

#count for the columns

    board[row][column]

    num = 0



# go to the first index in columns
# go to the first index and count through 1-9
