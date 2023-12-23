def solve():
    cards = open('puzzle2.txt', 'r').read().splitlines()

    copies = {i: 1 for i in range(len(cards))}
    
    for i, card in enumerate(cards):
        rightPart = card.split(":")[1:][0].split("|")
        winningNumbers = set(rightPart[0].split())
        numbers = set(rightPart[1].split())

        currentCopies = copies[i]
        matchingNumber = getMatchingNumber(winningNumbers, numbers)

        for count in range(1, matchingNumber + 1):
            copies[i + count] += currentCopies

    return sum(list(copies.values()))

def getMatchingNumber(winningNumbers, numbers):
    matchingNumber = 0

    for number in numbers:
        if number == "":
            continue
        if number in winningNumbers:
            matchingNumber += 1

    return matchingNumber

res = solve()
print(res)
