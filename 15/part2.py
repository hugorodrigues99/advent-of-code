def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()[0]

    res = 0
    strings = input.split(",")

    boxToLenses = {i: [] for i in range(256)}
    lenseToBox = {}

    for string in strings:
        processString(string, boxToLenses, lenseToBox)

    for box in boxToLenses:
        lenses = boxToLenses[box]
        for i, lense in enumerate(lenses):
            length = lenseToBox[lense][1]
            res += (box + 1) * (i + 1) * length

    return res

def getHash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256

    return hash

def processString(string, boxToLenses, lenseToBox):
    if "=" in string:
        equalIdx = string.index("=")
        label = string[:equalIdx]
        length = int(string[equalIdx + 1:])
        
        if label not in lenseToBox:
            box = getHash(label)
            lenseToBox[label] = [box, length]
            boxToLenses[box].append(label)
        else:
            lenseToBox[label][1] = length
    else: # "-"
        label = string[:-1]
        if label in lenseToBox:
            box = lenseToBox[label][0]
            boxToLenses[box].remove(label)
            del lenseToBox[label]

res = solve()
print(res)
