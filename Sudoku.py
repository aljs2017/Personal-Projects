'''
This code checks to see if a sudoku board is valid or not. Each "." represents an empty space.
'''


board_rows = int(input().strip())
board_columns = int(input().strip())

for _ in range(board_rows):
    board.append(list(map(int, input().rstrip().split())))


def ValidSudoku(board):
    for a in range(len(board)):

        ones = board[a].count('1')
        if ones > 1:
            return "The board is not valid."
        twos = board[a].count('2')
        if twos > 1:
            return "The board is not valid."
        threes = board[a].count('3')
        if threes > 1:
            return "The board is not valid."
        fours = board[a].count('4')
        if fours > 1:
            return "The board is not valid."
        fives = board[a].count('5')
        if fives > 1:
            return "The board is not valid."
        sixes = board[a].count('6')
        if sixes > 1:
            return "The board is not valid."
        sevens = board[a].count('7')
        if sevens > 1:
            return "The board is not valid."
        eights = board[a].count('8')
        if eights > 1:
            return "The board is not valid."
        nines = board[a].count('9')
        if nines > 1:
            return "The board is not valid."

    for b in range(len(board)):

        ones = board[0][b].count('1')
        if ones > 1:
            return "The board is not valid."
        twos = board[1][b].count('2')
        if twos > 1:
            return "The board is not valid."
        threes = board[2][b].count('3')
        if threes > 1:
            return "The board is not valid."
        fours = board[3][b].count('4')
        if fours > 1:
            return "The board is not valid."
        fives = board[4][b].count('5')
        if fives > 1:
            return "The board is not valid."
        sixes = board[5][b].count('6')
        if sixes > 1:
            return "The board is not valid."
        sevens = board[6][b].count('7')
        if sevens > 1:
            return "The board is not valid."
        eights = board[7][b].count('8')
        if eights > 1:
            return "The board is not valid."
        nines = board[8][b].count('9')
        if nines > 1:
            return "The board is not valid."

    return "The board is valid."


print(ValidSudoku(board))

