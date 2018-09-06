n = int(input())
ar = list(map(int, input().split()))
s = 0

for i in range(1, n):
    if (ar[i] > ar[i - 1]):
        s += 1
print(s)