def sec_lowGrade(class_list):
    sec_low_score = sorted(set(x[1] for x in class_list))[1]
    res = sorted([x[0] for x in class_list if x[1] == sec_low_score])
    return res

numStudents = int(input())
class_list = []

for i in range(numStudents):
    class_list.append([str(input()), float(input())])

print('\n'.join(sec_lowGrade(class_list)))