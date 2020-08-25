n, m = list(map(int, input().split()))


result = ''
count=1
for k in range(n):
    if k % 2:
        for j in range(m-1, -1, -1):

            result += '{} '.format(count + j)
        count += m
    else:
        for j in range(m):
            result += '{} '.format(count)
            count += 1
    result += '\n'

print(result)
