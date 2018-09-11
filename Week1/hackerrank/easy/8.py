def secLowGrade(classList):
    secLowScore = sorted(set(x[1] for x in classList))[1]
    res = sorted([x[0] for x in classList if x[1] == secLowScore])
    return res

numStudents = int(input())
classList = []

for i in range(numStudents):
    classList.append([str(input()), float(input())])

print('\n'.join(secLowGrade(classList)))