import math

def mini(a, b, c, d):
    return(min(a, b, c, d)) 

ar = list(map(int, input().split()))


print(mini(ar[0], ar[1], ar[2], ar[3]))