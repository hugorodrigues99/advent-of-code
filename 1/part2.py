specialTokens = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

def sumTokens(tokens):
    res = 0
    for token in tokens:
        left = 0
        leftDigit = ""
        while leftDigit == "":
            # Is digit
            if token[left].isdigit():
                leftDigit = token[left]
                break

            # Starts with special token
            for i, specialToken in enumerate(specialTokens):
                if token[left:].startswith(specialToken):
                    leftDigit = str(i + 1)
                    break

            left += 1
        
        right = len(token) - 1
        rightDigit = ""
        while rightDigit == "":
            # Is digit
            if token[right].isdigit():
                rightDigit = token[right]
                break

            # Starts with special token
            for i, specialToken in enumerate(specialTokens):
                if token[right:].startswith(specialToken):
                    rightDigit = str(i + 1)
                    break

            right -= 1

        res += int(leftDigit + rightDigit)

    return res

file = open('puzzle2.txt', 'r')
tokens = file.readlines()

print(sumTokens(tokens))
