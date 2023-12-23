def solve():
    input = open('puzzle2.txt', 'r').read().splitlines()

    reports = processReports(input)

    res = 0
    for report in reports:
        extrapolatedReport = extrapolateReport(report)
        res += calculateNewFirstValues(extrapolatedReport)

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

def calculateNewFirstValues(extrapolatedReports):
    extrapolatedReports[-1].insert(0, 0)

    for i in reversed(range(1, len(extrapolatedReports))):
        currentRow = extrapolatedReports[i]
        previousRow = extrapolatedReports[i - 1]

        previousRow.insert(0, previousRow[0] - currentRow[0])

    return extrapolatedReports[0][0]

res = solve()
print(res)
