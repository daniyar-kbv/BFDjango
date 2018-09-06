n = int(input())
ar = list(map(int, input().split()))
b = 0

for i in range(1, n - 1):
    if (ar[i + 1] < ar[i]) and (ar[i] > ar[i - 1]):
        b += 1
print(b)