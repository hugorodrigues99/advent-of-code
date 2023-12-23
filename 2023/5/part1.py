def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()
    seeds, almanac = processInput(input)
    res = float("inf")

    for seed in seeds:
        curr = seed

        for map in almanac:
            for destination, source, distance in map:
                if source <= curr < source + distance:
                    diff = curr - source
                    curr = destination + diff
                    break

        res = min(res, curr)   

    return res

def processInput(input):
    seeds = [int(value) for value in input[0].split()[1:]]

    almanac = []

    tokens = input[2:]
    tokens.append("") # Handle last case
    currentMap = []
    for token in tokens:
        if token == "":
            almanac.append(currentMap)
            currentMap = []
        elif token[0].isdigit():
            values = [int(value) for value in token.split()]
            currentMap.append(values)

    return seeds, almanac

res = solve()
print(res)
