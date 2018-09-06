n = int(input())
ar = list(map(int, input().split()))
s = 0

for element in ar:
    if element > 0:
        s += 1
print(s)