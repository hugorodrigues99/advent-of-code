def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()[0]

    res = 0
    strings = input.split(",")
    for string in strings:
        res += getHash(string)

    return res

def getHash(string):
    hash = 0
    for char in string:
        hash += ord(char)
        hash *= 17
        hash %= 256

    return hash

res = solve()
print(res)
