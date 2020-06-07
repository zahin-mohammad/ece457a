import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

maze = [
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1], 
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
            [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
def heuristic(currState, goalState):
    return (currState[0]-goalState[0])**2 + (currState[1] -goalState[1])**2

def aStar(state, goalState):
    pass

def bfs(initState, goalState):
    path, cost, goalReached = [], 0, False
    # maps state to its parent
    bfsMap = []

    stack = [initState]

    while len(stack):
        state = stack.pop()
        row = state[0]
        col = state[1]

        stateChildren = []
        if (row-1, col) not in bfsMap and row-1 >= 0:
            stack.append((row-1, col))
            bfsMap[(row-1, col)] = state

        if (row, col+1) not in bfsMap and col+1 < len(maze[0]):
            stack.append((row, col+1))
            bfsMap[(row, col+1)] = state

dfsMap = set()
def dfs(state, goalState): # Return Path, totalCost, goalReached 
    # Goal Step
    dfsMap.add(state)
    if state == goalState:
        return [state], 1, True

    # Not at Goal, go one level deeper
    row = state[0]
    col = state[1]

    # Add nodes to LIFO stack in order Up, Down, Left, Right
    # Therefore process in order of Right, Left, Down, Up

    # Move Right
    if (row, col+1) not in dfsMap and col +1 < len(maze[0]) and not maze[row][col+1]:
        path, cost, goalReached = dfs((row, col+1), goalState)
        if goalReached:
            newPath = [state]
            newPath.extend(path)
            return newPath, 1+cost, True
    # Move Left
    if (row, col-1) not in dfsMap and col -1 >=0 and not maze[row][col-1]:
        path, cost, goalReached = dfs((row, col-1), goalState)
        if goalReached:
            newPath = [state]
            newPath.extend(path)
            return newPath, 1+cost, True
    # Move Down
    if (row+1, col) not in dfsMap and row + 1 < len(maze) and not maze[row+1][col]:
        path, cost, goalReached = dfs((row+1, col), goalState)
        if goalReached:
            newPath = [state]
            newPath.extend(path)
            return newPath, 1+cost, True
    # Move Up
    if (row-1, col) not in dfsMap and row -1 >= 0 and not maze[row-1][col]:
        path, cost, goalReached = dfs((row-1, col), goalState)
        if goalReached:
            newPath = [state]
            newPath.extend(path)
            return newPath, 1+cost, True
    return [], -1, False









def convertToTopLeft(state):
    # 1,0 -> 24, 1
    return (len(maze)-1-state[1], state[0])

def convertToCartesian(state):
    # 24,1 -> 1,0
    return (state[1], len(maze)-1 - state[0])

def printColoredMaze(path, init, goal):
    pathSet = set(path)
    for i, row in enumerate(maze):
        rowString = ""
        for j, col in enumerate(row):
            if (i,j) == init or (i,j) == goal:
                rowString += (f"{bcolors.FAIL}\u2588{bcolors.ENDC}")
            elif (i,j) in pathSet:
                rowString += (f"{bcolors.OKGREEN}\u2588{bcolors.ENDC}")
            else:
                rowString += (f"{bcolors.OKBLUE}\u2588{bcolors.ENDC}") if col else  (f"{bcolors.WARNING}\u2588{bcolors.ENDC}")
        print(rowString)

def printPath(path):
    pathString = ""
    for coord in path:
        pathString += str(convertToCartesian(coord))
    print(pathString)


init = convertToTopLeft((0,0))
goal = convertToTopLeft((24,24))
print(convertToCartesian(init))
print(convertToCartesian(goal))

dfsPath, cost, goalReached = dfs(init, goal)
printColoredMaze(dfsPath, init, goal)
print(f"Cost: {cost}")
print(f"Visited: {len(dfsMap)}")
print("")
[print(convertToCartesian(state)) for state in dfsPath]


















# bfsPath = bfs((initRow, initCol))

# aStarPath = aStar((initRow, initCol))




















# initRow = int(input("Enter Initial Row : "))
# initCol = int(input("Enter Initial Col : "))

# if initRow >= len(maze) or initCol >= len(maze[0]) or maze[initRow][initCol]:
#     print("Invalid initial state")
#     sys.exit()
