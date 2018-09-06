n = int(input())
i = 2
mind = 1

while(i <= n):
    if(n % i == 0):
        mind = i
        print(i)
        break
    i = i + 1