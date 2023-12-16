UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()
    board = [[value for value in row] for row in input]

    return dfs(0, 0, board)

def dfs(i, j, board):
    visitedAndDirections = set()
    stack = [[i, j, RIGHT]]

    while len(stack) > 0:
        row, col, dir = stack.pop()

        if (row, col, dir[0], dir[1]) in visitedAndDirections:
            continue
    
        visitedAndDirections.add((row, col, dir[0], dir[1]))

        for nRow, nCol, nDir in getNeighbors(row, col, board, dir):
            if (nRow, nCol, nDir[0], nDir[1]) in visitedAndDirections:
                continue

            stack.append([nRow, nCol, nDir])

    visited = set([(row, col) for row, col, _, _ in visitedAndDirections])
    return len(visited)


def getNeighbors(i, j, board, direction):
    neighbors = []

    symbol = board[i][j]
    
    if symbol == ".":
        neighbors.append([i + direction[0], j + direction[1], direction])
    elif symbol == "|":
        if direction == UP or direction == DOWN:
            neighbors.append([i + direction[0], j + direction[1], direction])
        else:
            neighbors.append([i - 1, j, UP])
            neighbors.append([i + 1, j, DOWN])
    elif symbol == "-":
        if direction == LEFT or direction == RIGHT:
            neighbors.append([i + direction[0], j + direction[1], direction])
        else:
            neighbors.append([i, j - 1, LEFT])
            neighbors.append([i, j + 1, RIGHT])
    elif symbol == "/":
        if direction == UP:
            neighbors.append([i, j + 1, RIGHT])
        elif direction == DOWN:
            neighbors.append([i, j - 1, LEFT])
        elif direction == LEFT:
            neighbors.append([i + 1, j, DOWN])
        else: # RIGHT
            neighbors.append([i - 1, j, UP])
        
    else: # "\"
        if direction == UP:
            neighbors.append([i, j - 1, LEFT])
        elif direction == DOWN:
            neighbors.append([i, j + 1, RIGHT])
        elif direction == LEFT:
            neighbors.append([i - 1, j, UP])
        else: # RIGHT
            neighbors.append([i + 1, j, DOWN])
        
    return [[nRow, nCol, nDir] for nRow, nCol, nDir in neighbors if not isOutOfBounds(nRow, nCol, board)]

def isOutOfBounds(i, j, board):
    return i < 0 or i >= len(board) or j < 0 or j >= len(board[0])

res = solve()
print(res)
