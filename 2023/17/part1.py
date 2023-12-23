from heapq import heappush, heappop

DIRECTIONS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

MAX_SAME_DIRECTION_STEPS = 3

def solve(filename):
    input = open(filename, 'r').read().splitlines()
    matrix = [[int(value) for value in row] for row in input]
    return dijkstra(matrix)

def dijkstra(matrix):
    seen = set()
    minHeap = [(0, 0, 0, 0, 0, 0)] # heat, i, j, direction row, direction col, direction steps streak

    while len(minHeap) > 0:
        heat, i, j, di, dj, streak = heappop(minHeap)

        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            return heat
        
        if (i, j, di, dj, streak) in seen:
            continue

        seen.add((i, j, di, dj, streak))

        for nRow, nCol, ndi, ndj in getNeighbors(i, j, matrix, di, dj, streak):
            nHeat = heat + matrix[nRow][nCol]
            nStreak = streak + 1 if (di, dj) == (ndi, ndj) else 1
            heappush(minHeap, (nHeat, nRow, nCol, ndi, ndj, nStreak))

    return float("inf") # Should never get here

def getNeighbors(i, j, matrix, di, dj, streak):
    neighbors = []

    for ndi, ndj in getPossibleDirections(di, dj, streak):
        row = i + ndi
        col = j + ndj
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            neighbors.append((row, col, ndi, ndj))

    return neighbors

def getPossibleDirections(di, dj, streak):
    if (di, dj) == (0, 0):
        return DIRECTIONS
    
    directions = []

    if streak < MAX_SAME_DIRECTION_STEPS:
        directions.append((di, dj))

    for direction in DIRECTIONS:
        if direction != (di, dj) and direction != (-di, -dj):
            directions.append(direction)

    return directions

res_final = solve("puzzle1.txt")
print(res_final)
