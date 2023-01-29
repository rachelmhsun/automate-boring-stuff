# Conway's Game of Life
import random, time, copy
width = 60
height = 20

# Create list of list for cells
nextCells = []
for x in range(width):
    column = [] # create new column
    for y in range(height):
        if random.randint(0,1) == 0:
        # if (x,y) in ((1,0),(2,1),(0,2),(1,2),(2,2)):
            column.append('#') # add living cell
        else:
            column.append('') # add dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True:
    # print('\n\n\n\n\n') # separate each step with newlines
    print('~~~~~')
    currentCells = copy.deepcopy(nextCells)
    # print currentCells on screen
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='') # print the # or space
        print() # print newline at end of row

    # calculate next step's cells based on current step's cells
    for x in range(width):
        for y in range(height):
            # get neighboring coordinates
            # '% width' ensures leftCoord is always between 0 and width - 1
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height

            # count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive


            # set cell based on Conway's Game of Life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#' # living cells with 2 or 3 neighbors stay alive
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#' # dead cells with 3 neighbors become alive
            else:
                nextCells[x][y] = ' ' # everything else stays dead
    time.sleep(1)
