def solve():
    input = open('puzzle1.txt', 'r').read().splitlines()

    reports = processReports(input)

    res = 0
    for report in reports:
        extrapolatedReport = extrapolateReport(report)
        res += calculateNewLastValues(extrapolatedReport)

    return res

def processReports(input):
    reports = []
    for row in input:
        reports.append([int(value) for value in row.split(" ")])

    return reports

def extrapolateReport(report):
    extrapolatedReport = [report[:]]

    while not areAllZeroes(extrapolatedReport[-1]):
        newRow = []
        for i in range(len(extrapolatedReport[-1]) - 1):
            currentValue = extrapolatedReport[-1][i]
            nextValue = extrapolatedReport[-1][i + 1]

            newRow.append(nextValue - currentValue)

        extrapolatedReport.append(newRow)

    return extrapolatedReport

def areAllZeroes(report):
    for value in report:
        if value != 0:
            return False
        
    return True

def calculateNewLastValues(extrapolatedReports):
    extrapolatedReports[-1].append(0)

    for i in reversed(range(1, len(extrapolatedReports))):
        currentRow = extrapolatedReports[i]
        previousRow = extrapolatedReports[i - 1]

        previousRow.append(currentRow[-1] + previousRow[-1])

    return extrapolatedReports[0][-1]

res = solve()
print(res)
