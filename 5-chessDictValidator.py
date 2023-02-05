# Chess Dictionary Validator
# checkChessDict function performs very basic check:
# 1) proper number of chess pieces on board
# 2) checks if space is valid (i.e., a possible board space 1-8 and a-h)


def checkChessDict(board):
    spacecols = ["1", "2", "3", "4", "5", "6", "7", "8"]  # reference column list
    spacerows = ["a", "b", "c", "d", "e", "f", "g", "h"]  # reference row list
    count = {  # reference piece list with counts initialized at zero
        "bking": 0,
        "wking": 0,
        "wqueen": 0,
        "bqueen": 0,
        "bbishop": 0,
        "wbishop": 0,
        "wknight": 0,
        "bknight": 0,
        "wpawn": 0,
        "bpawn": 0,
        "brook": 0,
        "wrook": 0,
    }
    # check if each input board space is on board
    for key in board.keys():
        col = key[0]
        row = key[1]
        if row not in spacerows:
            print(row)
            return False
        if col not in spacecols:
            print(col)
            return False

    # check if each input piece is valid piece
    # if so, add to running count
    for value in board.values():
        if value not in count.keys():
            return False
        else:
            count[value] += 1
    # print(count)

    # once count done, check if there are too many of each piece
    if (count["wking"] > 1) or (count["bking"] > 1):
        print("Too many kings")
        return False
    elif (count["wqueen"] > 1) or (count["bqueen"] > 1):
        print("Too many queens")
        return False
    elif (count["bpawn"] > 8) or (count["wpawn"] > 8):
        print("Too many pawns")
        return False
    elif (count["bbishop"] > 2) or (count["wbishop"] > 2):
        print("Too many bishops")
        return False
    elif (count["wknight"] > 2) or (count["bknight"] > 2):
        print("Too many knights")
        return False
    elif (count["wrook"] > 2) or (count["brook"] > 2):
        print("Too many rooks")
        return False
    else:
        print("This is a valid board!")
        return True


# input board
myBoard = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}
# check board
checkChessDict(myBoard)
