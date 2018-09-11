n = int(input())

ar = list(map(int, input().split()))
b = max(ar)

while b in ar: ar.remove(b)

print(max(ar))