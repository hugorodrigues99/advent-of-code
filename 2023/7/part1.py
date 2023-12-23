from functools import cmp_to_key

POINTS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()
    hands = [[hand[:5], int(hand[6:])] for hand in input]

    # 0: high card
    # 1: one pair
    # 2: two pair
    # ...
    # 5: four of a kind
    # 6: five of a kind
    types = [[] for _ in range(7)]

    for i in range(len(hands)):
        hand = hands[i][0]
        occurrences = getOccurrences(hand)
        if isHighCard(hand, occurrences):
            types[0].append(i)
        elif isOnePair(hand, occurrences):
            types[1].append(i)
        elif isTwoPair(hand, occurrences):
            types[2].append(i)
        elif isThreeOfAKind(hand, occurrences):
            types[3].append(i)
        elif isFullHouse(hand, occurrences):
            types[4].append(i)
        elif isFourOfAKind(hand, occurrences):
            types[5].append(i)
        elif isFiveOfAKind(hand, occurrences):
            types[6].append(i)

    rank = 1
    res = 0
    for i in range(len(types)):
        types[i].sort(key=cmp_to_key(lambda x, y: pointsCompare(hands[x][0], hands[y][0])))

        for idx in types[i]:
            res += hands[idx][1] * rank
            rank += 1

    return res


def getOccurrences(hand):
    occurrences = {}
    for card in hand:
        if card not in occurrences:
            occurrences[card] = 0
        occurrences[card] += 1

    return occurrences

def getNumberOfCardsWithOccurrences(hand, occurrences, occurrencesNumber):
    numberOfCardsWithOccurrences = 0
    for card in set(hand):
        if occurrences[card] == occurrencesNumber:
            numberOfCardsWithOccurrences += 1

    return numberOfCardsWithOccurrences

def pointsCompare(hand1, hand2):
    for i in range(len(hand1)):
        card1 = hand1[i]
        card2 = hand2[i]
        if card1 != card2:
            return POINTS[card1] - POINTS[card2]

def isHighCard(hand, occurrences):
    return len(set(hand)) == 5

def isOnePair(hand, occurrences):
    return len(set(hand)) == 4

def isTwoPair(hand, occurrences):
    if len(set(hand)) != 3:
        return False
    
    return getNumberOfCardsWithOccurrences(hand, occurrences, 2) == 2

def isThreeOfAKind(hand, occurrences):
    if len(set(hand)) != 3:
        return False

    return getNumberOfCardsWithOccurrences(hand, occurrences, 3) == 1 and getNumberOfCardsWithOccurrences(hand, occurrences, 1) == 2

def isFullHouse(hand, occurrences):
    if len(set(hand)) != 2:
        return False

    return getNumberOfCardsWithOccurrences(hand, occurrences, 3) == 1 and getNumberOfCardsWithOccurrences(hand, occurrences, 2) == 1

def isFourOfAKind(hand, occurrences):
    if len(set(hand)) != 2:
        return False

    return getNumberOfCardsWithOccurrences(hand, occurrences, 4) == 1

def isFiveOfAKind(hand, occurrences):
    return len(set(hand)) == 1

res = solve()
print(res)
