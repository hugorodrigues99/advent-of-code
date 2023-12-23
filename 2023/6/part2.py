def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()

    time = int("".join(input[0][5:].split()))
    distance = int("".join(input[1][9:].split()))
    
    wonRaces = 0
    for holdTime in range(time + 1):
        timeRunning = time - holdTime
        speed = holdTime
        currentDistance = timeRunning * speed

        if currentDistance > distance:
            wonRaces += 1
    
    return wonRaces

res = solve()
print(res)
