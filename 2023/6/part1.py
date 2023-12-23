def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()

    times = [int(time) for time in input[0][5:].split()]
    distances = [int(distance) for distance in input[1][9:].split()]

    res = 1
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        wonRaces = 0
        for holdTime in range(time + 1):
            timeRunning = time - holdTime
            speed = holdTime
            currentDistance = timeRunning * speed

            if currentDistance > distance:
                wonRaces += 1

        res *= wonRaces
    
    return res

res = solve()
print(res)
