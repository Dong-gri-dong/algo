n = list(map(int, input().split()))

result = [0]*11
for i in n:
    if i == 0:
        break

    if 0 < i <= 100:
        result[ i//10 ] += 1



for i in range(10, -1, -1):
    if result[i] != 0:
        print('{} : {} person'.format((i)*10, result[i]))




