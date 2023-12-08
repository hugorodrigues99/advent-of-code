def sumTokens(tokens):
    res = 0
    for token in tokens:
        left = 0
        while left < len(token) and not token[left].isdigit():
            left += 1

        right = len(token) - 1
        while right >= 0 and not token[right].isdigit():
            right -= 1

        res += int(token[left] + token[right])

    return res

file = open('puzzle1.txt', 'r')
tokens = file.readlines()

print(sumTokens(tokens))
