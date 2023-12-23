DIRS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

ENCODING = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

def solve(filename):
    input = open(filename, 'r').read().splitlines()
    points, boundaryPointsNumber = getPoints(input)
    area = getArea(points)
    insidePointsNumber = getInsidePointsNumber(area, boundaryPointsNumber)

    return insidePointsNumber + boundaryPointsNumber
    
def getPoints(input):
    points = [(0, 0)]
    boundaryPointsNumber = 0

    for line in input:
        _, _, color = line.split(" ")
        hex = color[2:-1]
        encodedDirection = hex[-1]
        steps = int(hex[:-1], base=16)

        boundaryPointsNumber += steps
        d = ENCODING[encodedDirection]
        i, j = points[-1]
        di, dj = DIRS[d]

        points.append((i + di * steps, j + dj * steps))


    return points, boundaryPointsNumber

# Shoelace formula
def getArea(points):
    area = 0
    for i in range(len(points)):
        x = points[i][0]
        y1 = points[i - 1][1]
        y2 = points[(i + 1) % len(points)][1]

        area += x * (y1 - y2)

    return abs(area) // 2

# Pick's theorem
def getInsidePointsNumber(area, boundaryPointsNumber):
    return area - (boundaryPointsNumber // 2) + 1

res_final = solve("puzzle2.txt")
print(res_final)
