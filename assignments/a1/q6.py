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
    # Euclidean distance
    return (currState[0]-goalState[0])**2 + (currState[1] -goalState[1])**2

def aStar(initState, goalState):
    path, nodesVisited, nodesExpanded, goalReached = [], 1, 1, False
    # maps state to its parent
    bfsMap = {}

    # Stack stores elements in the form of (heuristic, row, col)
    # Stored in Descending order
    stack = [(heuristic(initState, goalState), initState[0], initState[1])]

    while len(stack):
        state = stack.pop()
        nodesExpanded +=1
        if (state[1], state[2]) == goalState:
            goalReached = True
            break
        row = state[1]
        col = state[2]
        
        # Move Up
        if (row-1, col) not in bfsMap and row-1 >= 0 and not maze[row-1][col]:
            nodesVisited +=1
            childCost = heuristic((row-1, col), goalState)
            stack.append((childCost, row-1, col))
            bfsMap[(row-1, col)] = (row, col)
        
        # Move Down
        if (row+1, col) not in bfsMap and row+1 < len(maze) and not maze[row+1][col]:
            nodesVisited +=1
            childCost = heuristic((row+1, col), goalState)
            stack.append((childCost, row+1, col))
            bfsMap[(row+1, col)] = (row, col)
        
        # Move Left 
        if (row, col-1) not in bfsMap and col-1 >= 0 and not maze[row][col-1]:
            nodesVisited +=1
            childCost = heuristic((row, col-1), goalState)
            stack.append((childCost, row, col-1))
            bfsMap[(row, col-1)] = (row, col)

        # Move Right
        if (row, col+1) not in bfsMap and col+1 < len(maze[0]) and not maze[row][col+1]:
            nodesVisited +=1
            childCost = heuristic((row, col+1), goalState)
            stack.append((childCost, row, col+1))
            bfsMap[(row, col+1)] = (row, col)

        stack.sort(reverse=True)
    
    if not goalReached:
        return path, nodesVisited, goalReached
    
    path.append(goalState)
    cost = 1
    traverseState = bfsMap[goalState]
    while True:
        cost +=1
        path.append(traverseState)
        if traverseState == initState:
            break
        else:
            traverseState = bfsMap[traverseState]

    return list(reversed(path)), nodesVisited, nodesExpanded, goalReached
    
def bfsOrDfs(initState, goalState, isBfs):
    path, nodesVisited, nodesExpanded, goalReached = [], 1, 1, False
    # maps state to its parent
    bfsMap = {}

    stack = [initState]

    while len(stack):
        state = stack.pop(0) if isBfs else stack.pop()
        nodesExpanded +=1
        if state == goalState:
            goalReached = True
            break
        row = state[0]
        col = state[1]
        stateChildren = []
        
        # Move Up
        if (row-1, col) not in bfsMap and row-1 >= 0 and not maze[row-1][col]:
            nodesVisited+=1
            stack.append((row-1, col))
            bfsMap[(row-1, col)] = state
        
        # Move Down
        if (row+1, col) not in bfsMap and row+1 < len(maze) and not maze[row+1][col]:
            nodesVisited+=1
            stack.append((row+1, col))
            bfsMap[(row+1, col)] = state
        
        # Move Left 
        if (row, col-1) not in bfsMap and col-1 >= 0 and not maze[row][col-1]:
            nodesVisited+=1
            stack.append((row, col-1))
            bfsMap[(row, col-1)] = state

        # Move Right
        if (row, col+1) not in bfsMap and col+1 < len(maze[0]) and not maze[row][col+1]:
            nodesVisited+=1
            stack.append((row, col+1))
            bfsMap[(row, col+1)] = state
    
    if not goalReached:
        return path, nodesVisited, goalReached
    
    path.append(goalState)
    cost = 1
    traverseState = bfsMap[goalState]
    while True:
        cost +=1
        path.append(traverseState)
        if traverseState == initState:
            break
        else:
            traverseState = bfsMap[traverseState]

    return list(reversed(path)), nodesVisited, nodesExpanded, goalReached

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
            if (i,j) == init:
                rowString += (f"{bcolors.HEADER}\u2588{bcolors.ENDC}")
            elif (i,j) == goal:
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

def test(init, goal):
    dfsPath, visited, expanded, goalReached = bfsOrDfs(init, goal, False)
    print(f"DFS: {convertToCartesian(init)} -> {convertToCartesian(goal)}")
    print(f"Cost: {len(dfsPath)}")
    print(f"Visited: {visited}")
    print(f"Expanded: {expanded}")
    print("")
    printColoredMaze(dfsPath, init, goal)
    print("")
    printPath(dfsPath)
    print("")

    bfsPath, visited, expanded, goalReached = bfsOrDfs(init, goal, True)
    print(f"BFS: {convertToCartesian(init)} -> {convertToCartesian(goal)}")
    print(f"Cost: {len(bfsPath)}")
    print(f"Visited: {visited}")
    print(f"Expanded: {expanded}")
    print("")
    printColoredMaze(bfsPath, init, goal)
    print("")
    printPath(bfsPath)
    print("")

    aStarPath, visited, expanded, goalReached = aStar(init, goal)
    print(f"A*: {convertToCartesian(init)} -> {convertToCartesian(goal)}")
    print(f"Cost: {len(aStarPath)}")
    print(f"Visited: {visited}")
    print(f"Expanded: {expanded}")
    print("")
    printColoredMaze(aStarPath, init, goal)
    print("")
    printPath(aStarPath)
    print("")


init = convertToTopLeft((0,0))
goal = convertToTopLeft((24,24))
test(init, goal)

init = convertToTopLeft((2,11))
goal = convertToTopLeft((2,21))
test(init, goal)

init = convertToTopLeft((2,11))
goal = convertToTopLeft((23,19))
test(init, goal)