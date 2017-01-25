board = []
rows = 8
cols = 8

def main():
    for r in range(0,rows):
        board.append([])
        for c in range(0,cols):
            board[r].append(' ')

    placeQueens(0)
    printBoard()

# try and place the queens starting with the column number
def placeQueens(col):
    # if we get here, return true -- we were able to place a queen
    if (col >= cols):
        return True
    else:
        placed = False
        row = 0
        # start at row 0, and loop while we haven't been able to finish
        while (not placed and row < rows):
            # if we're under attack at this location, try the next row
            if (isUnderAttack((row,col))):
                # move to the next row
                row += 1
            else: # otherwise, we need to see about placing the queen here and seeing if the remaining columns will work
                # set the queen and try again
                placeQueen((row,col))
                # recursive call using next column
                placed = placeQueens(col + 1)
                # if we could not place (we ran out of columns for this row), remove this queen and try another row
                if (not placed):
                    removeQueen((row,col))
                    row += 1

        return placed

# are we under attack?
def isUnderAttack(coord):
    # row
    for c in range(0,cols):
        if board[coord[0]][c] == 'X':
            return True

    # col
    for r in range(0,rows):
        if board[r][coord[1]] == 'X':
            return True

    # up/left
    r = coord[0]-1
    c = coord[1]-1
    while (r >= 0 and c >= 0):
        if board[r][c] == 'X':
            return True
        r -=1
        c -=1
    # up/right
    r = coord[0] - 1
    c = coord[1] + 1
    while (r >= 0 and c < cols):
        if board[r][c] == 'X':
            return True
        r -= 1
        c += 1
    # down/left
    r = coord[0] + 1
    c = coord[1] - 1
    while (r < rows and c >= 0):
        if board[r][c] == 'X':
            return True
        r += 1
        c -= 1

    # down/right
    r = coord[0] + 1
    c = coord[1] + 1
    while (r < rows and c < cols):
        if board[r][c] == 'X':
            return True
        r += 1
        c += 1

    return False


def placeQueen(coord):
    board[coord[0]][coord[1]] = 'X'

def removeQueen(coord):
    board[coord[0]][coord[1]] = ' '

def printBoard():
    for r in board:
        print r


if __name__ == "__main__":
    main()