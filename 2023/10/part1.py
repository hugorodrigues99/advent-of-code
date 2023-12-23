PIPES_POSITIONS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
    "S": [(-1, 0), (1, 0), (0, 1), (0, -1)]
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

            for neighborRow, neighborCol in neighbors:
                if (neighborRow, neighborCol) in visited:
                    continue

                if canTakeNeighbor(i, j, neighborRow, neighborCol, matrix):
                    queue.append([neighborRow, neighborCol])

        steps += 1

    return steps - 1

def getNeighbors(i, j, matrix):
    neighbors = []
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    for neighborRow, neighborCol in directions:
        newRow = i + neighborRow
        newCol = j + neighborCol

        if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]):
            neighbors.append([newRow, newCol])

    return neighbors

def canTakeNeighbor(i, j, neighborRow, neighborCol, matrix):
    currentPipe = matrix[i][j]
    neighborPipe = matrix[neighborRow][neighborCol]

    positionsConnectedToCurrent = [(i + row, j + col) for (row, col) in PIPES_POSITIONS[currentPipe]]
    positionsConnectedToNeighbor = [(neighborRow + row, neighborCol + col) for (row, col) in PIPES_POSITIONS[neighborPipe]]

    return (neighborRow, neighborCol) in positionsConnectedToCurrent and (i, j) in positionsConnectedToNeighbor


res = solve()
print(res)
