def validateGames(games):
    res = 0
    for game in games:
        array = game.split()
        gameId = int(array[1].split(":")[0])
        array = array[2:]

        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for i in range(1, len(array), 2):
            color = array[i].split(",")[0].split(";")[0]
            count = int(array[i - 1])

            if color == "red":
                maxRed = max(maxRed, count)
            elif color == "green":
                maxGreen = max(maxGreen, count)
            else:
                maxBlue = max(maxBlue, count)

        power = maxRed * maxGreen * maxBlue
        res += power
        
    return res


file = open('puzzle2.txt', 'r')
games = file.readlines()
res = validateGames(games)
print(res)
