ALL_DIRECTIONS = [(0, -1), (0, 1), (-1 ,0), (1, 0)]

def solve(filename):
    input = open(filename, 'r').read().splitlines()
    matrix = [[value for value in row] for row in input]

    startPoint, endPoint, points = getPoints(matrix)
    graph = buildGraph(points, matrix)
    return dfs(startPoint, endPoint, graph, set())

def getPoints(matrix):
    startPoint = (0, matrix[0].index("."))
    endPoint = (len(matrix) - 1, matrix[-1].index("."))

    points = [startPoint, endPoint]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                continue

            neighbors = 0
            for nRow, nCol in getNeighbors(i, j, matrix):
                if matrix[nRow][nCol] != "#":
                    neighbors += 1
            
            if neighbors >= 3:
                points.append((i, j))
    
    return startPoint, endPoint, points

def buildGraph(points, matrix):
    graph = {point: {} for point in points}

    for i, j in points:
        stack = [(i, j, 0)]
        seen = {(i, j)}

        while len(stack) > 0:
            r, c, n = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(i, j)][(r, c)] = n
                continue

            for nRow, nCol in getNeighbors(r, c, matrix):
                if matrix[nRow][nCol] != "#" and (nRow, nCol) not in seen:
                    stack.append((nRow, nCol, n + 1))
                    seen.add((nRow, nCol))

    return graph

def getNeighbors(i, j, matrix):
    neighbors = []

    for directionX, directionY in ALL_DIRECTIONS:
        nRow = i + directionX
        nCol = j + directionY
        if inBounds(nRow, nCol, matrix):
            neighbors.append((nRow, nCol))

    return neighbors

def inBounds(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

def dfs(point, endPoint, graph, seen):
    if point == endPoint:
        return 0

    res = float("-inf")

    seen.add(point)
    for nPoint in graph[point]:    
        if nPoint in seen:
            continue
        
        res = max(res, dfs(nPoint, endPoint, graph, seen) + graph[point][nPoint])
        
    seen.remove(point)

    return res

res_test = solve("test.txt")
print(res_test)

res_final = solve("puzzle.txt")
print(res_final)
