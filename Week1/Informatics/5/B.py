def power(a, n):
    b = 1
    for i in range(n):
        b = b * a
    
    return b
ar = list(map(float, input().split()))
print(power(ar[0], int(ar[1])))