def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()
    seeds, almanac = processInput(input)

    for map in almanac:
        newSeeds = []
        while len(seeds) > 0:
            seedStart, seedEnd = seeds.pop()
            foundOverlap = False
            for destination, source, range in map:
                overlapStart = max(seedStart, source)
                overlapEnd = min(seedEnd, source + range)
                if overlapStart < overlapEnd: # Range overlap
                    foundOverlap = True
                    newSeeds.append([overlapStart - source + destination, overlapEnd - source + destination])
                    if overlapStart > seedStart:
                        seeds.append([seedStart, overlapStart])
                    if overlapEnd < seedEnd:
                        seeds.append([overlapEnd, seedEnd])
                    break
            
            if not foundOverlap:
                newSeeds.append([seedStart, seedEnd])
        
        seeds = newSeeds
    
    return min(seeds)[0]

def processInput(input):
    seeds = [int(value) for value in input[0].split()[1:]]
    processedSeeds = processSeeds(seeds)

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

    return processedSeeds, almanac

def processSeeds(seeds):
    seedRanges = []
    for i in range(0, len(seeds), 2):
        startSeed = seeds[i]
        distance = seeds[i + 1]
        seedRanges.append([startSeed, startSeed + distance])

    return seedRanges

res = solve()
print(res)
