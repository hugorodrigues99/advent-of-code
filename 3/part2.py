def solve():
    engine = open('puzzle2.txt', 'r').read().splitlines()

    visited = [[False for _ in range(len(engine[0]))] for _ in range(len(engine))]
    res = 0
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if isGearSymbol(engine[i][j]):
                res += checkNeighbors(i, j, engine, visited)

    return res

def checkNeighbors(i, j, engine, visited):
    partValues = []

    digitNeighbors = getDigitNeighbors(i, j, engine)
    for row, col in digitNeighbors:
        if not visited[row][col]:
            partValues.append(extendValue(row, col, engine, visited))

    if len(partValues) != 2:
        return 0
    
    return partValues[0] * partValues[1]

def extendValue(i, j, engine, visited):
    left = j
    while left >= 0 and engine[i][left].isdigit():
        visited[i][left] = True
        left -= 1

    right = j + 1
    while right < len(engine[0]) and engine[i][right].isdigit():
        visited[i][right] = True
        right += 1

    value = int(engine[i][left + 1: right])
    return value


def getDigitNeighbors(i, j, engine):
    neighbors = []
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for direction in directions:
        row = i + direction[0]
        col = j + direction[1]

        if 0 <= row < len(engine) and 0 <= col < len(engine[0]) and engine[row][col].isdigit():
            neighbors.append([row, col])

    return neighbors

def isGearSymbol(char):
    return char == "*"


res = solve()
print(res)
