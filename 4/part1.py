def solve():
    cards = open('puzzle1.txt', 'r').read().splitlines()
    
    res = 0

    for card in cards:
        rightPart = card.split(":")[1:][0].split("|")
        winningNumbers = set(rightPart[0].split())
        numbers = set(rightPart[1].split())

        res += getCardPoints(winningNumbers, numbers)

    return res

def getCardPoints(winningNumbers, numbers):
    cardPoints = 0

    for number in numbers:
        if number == "":
            continue
        if number in winningNumbers:
            if cardPoints != 0:
                cardPoints *= 2
            else:
                cardPoints = 1

    return cardPoints

res = solve()
print(res)
