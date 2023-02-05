# Character Picture Grid
import random

height = 8
width = 10


def printGrid(myGrid):
    ht = len(myGrid)
    wd = len(myGrid[0])
    for w in range(wd):
        for h in range(ht):
            print(myGrid[h][w], end="")
        print("")


# randomly seed a m x n grid
grid = []
for m in range(height):
    row = []
    for n in range(width):
        newchar = random.randint(0, 1)
        if newchar == 0:
            row.append("0")
        else:
            row.append(".")
    grid.append(row)
print(grid)

printGrid(grid)
