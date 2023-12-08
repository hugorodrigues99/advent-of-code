def validateGames(games):
    res = 0
    for game in games:
        array = game.split()
        gameId = int(array[1].split(":")[0])
        array = array[2:]

        isValid = True
        for i in range(1, len(array), 2):
            color = array[i].split(",")[0].split(";")[0]
            count = int(array[i - 1])

            invalidRed = color == "red" and count > 12
            invalidGreen = color == "green" and count > 13
            invalidBlue = color == "blue" and count > 14
            if invalidRed or invalidGreen or invalidBlue:
                isValid = False
                break

        if isValid:
            res += gameId
        
    return res



file = open('puzzle1.txt', 'r')
games = file.readlines()
res = validateGames(games)
print(res)
