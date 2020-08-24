n = list(map(int, input().split()))



for i in range(8):
    n.append( (n[i]+n[i+1]) %10)


for i in n:
    print(i, end=' ')

