n = int(input())
ar = list(map(int, input().split()))

for i in range(1, n):
    if ar[i] * ar[i - 1] > 0:
        print("YES")
        break
else:
    print("NO")