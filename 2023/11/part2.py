EXPANSION = 1_000_000

def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()
    matrix = [[value for value in row] for row in input]

    galaxies = getGalaxies(matrix)
    emptyRows = getEmptyRows(matrix)
    emptyCols = getEmptyCols(matrix)

    res = 0

    for i in range(len(galaxies)):
        curr = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            other = galaxies[j]
            
            minRow = min(curr[0], other[0])
            maxRow = max(curr[0], other[0])
            for row in range(minRow, maxRow):
                res += EXPANSION if row in emptyRows else 1

            minCol = min(curr[1], other[1])
            maxCol = max(curr[1], other[1])
            for col in range(minCol, maxCol):
                res += EXPANSION if col in emptyCols else 1
    
    return res

def getEmptyRows(matrix):
    emptyRows = set()
    for i in range(len(matrix)):
        if isEmpty(matrix[i]):
            emptyRows.add(i)

    return emptyRows

def getEmptyCols(matrix):
    emptyCols = set()
    for j in range(len(matrix[0])):
        if isEmpty([row[j] for row in matrix]):
            emptyCols.add(j)

    return emptyCols

def isEmpty(array):
    for value in array:
        if value != ".":
            return False
        
    return True

def getGalaxies(matrix):
    galaxies = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                galaxies.append([i, j])

    return galaxies

def printMatrix(matrix):
    for row in matrix:
        print("".join(row))

res = solve()
print(res)
