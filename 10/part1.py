EAST = "east"
WEST = "west"
NORTH = "north"
SOUTH = "south"

OPPOSITE_DIRECTIONS = {
    EAST: WEST,
    WEST: EAST,
    NORTH: SOUTH,
    SOUTH: NORTH
}

SYMBOLS_DIRECTIONS = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": [],
    "S": [NORTH, SOUTH, EAST, WEST]
}

def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()
    
    matrix = [[char for char in row] for row in input]
    startRow, startCol = getStartingPosition(matrix)
    return bfs(startRow, startCol, matrix)

def getStartingPosition(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                return [i, j]
    
    return [-1, -1] # Should never get here

def bfs(startRow, startCol, matrix):
    visited = set()
    
    steps = 0
    queue = [[startRow, startCol]]

    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            i, j = queue.pop(0)

            if (i, j) in visited:
                continue

            visited.add((i, j))
            neighbors = getNeighbors(i, j, matrix)

            for neighborRow, neighborCol, neighborDirection in neighbors:
                if (neighborRow,neighborCol) in visited:
                    continue

                if canTakeNeighbor(i, j, neighborRow, neighborCol, neighborDirection, matrix):
                    queue.append([neighborRow, neighborCol])

        steps += 1

    return steps - 1

def getNeighbors(i, j, matrix):
    neighbors = []
    directions = [[0, 1, EAST], [0, -1, WEST], [1, 0, SOUTH], [-1, 0, NORTH]]
    
    for neighborRow, neighborCol, neighborDirection in directions:
        newRow = i + neighborRow
        newCol = j + neighborCol

        if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]):
            neighbors.append([newRow, newCol, neighborDirection])

    return neighbors

def canTakeNeighbor(i, j, neighborRow, neighborCol, neigborDirection, matrix):
    currentSymbol = matrix[i][j]
    neighborSymbol = matrix[neighborRow][neighborCol]

    currentDirections = SYMBOLS_DIRECTIONS[currentSymbol]
    neighborDirections = SYMBOLS_DIRECTIONS[neighborSymbol]

    return neigborDirection in currentDirections and OPPOSITE_DIRECTIONS[neigborDirection] in neighborDirections


res = solve()
print(res)
