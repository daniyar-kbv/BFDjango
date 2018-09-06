def xor(a, b):
    if (a == b):
        return 0
    else:
        return 1
ar = list(map(int, input().split()))
print(xor(ar[0], ar[1]))