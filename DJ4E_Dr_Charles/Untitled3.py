#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #adding a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # nextCells is a list of colum lists
while True: # main loop
    print('\n\n\n\n\n') # Separate each step with newline
    currentCells = copy.deepcopy(nextCells)
    
    # Print current cell
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    
    # Cal the next step cells based on current step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            
            # Count living neightbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-left alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 #top right alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #left alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom left alve
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom right alive
            
            # Set cell based on COnway's game of life rule
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbor == 3):
                #living cells with 2,3 neightbor will alive
                nextcells[x][y] == '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cell become alive
                nextCells[x][y] = '#'
            else:
                # everything else stay dead
                nextCells = ' '
    time.sleep(1)   

