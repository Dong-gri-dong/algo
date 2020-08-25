n, m = list(map(int, input().split()))


result = ''
count=1
for k in range(n):
    for j in range(m):
        result += '{} '.format(count)
        count += 1
    result += '\n'

print(result)
