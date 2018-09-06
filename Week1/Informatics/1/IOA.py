import math

a = float(input())
b = float(input())
if a > 0 and b > 0 and a < 1000 and b < 1000:
    res = float(math.sqrt(pow(a, 2) + pow(b, 2)))
print(res)