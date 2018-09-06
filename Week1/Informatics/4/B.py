n = int(input())
ar = list(map(int, input().split()))

for element in ar:
    if element % 2 == 0:
        print(element)