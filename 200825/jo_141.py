n = int(input())


for i in range(1, 101):
    if i % n == 0:
        print(i, end=' ')
        if i % 10 ==0:
            break

