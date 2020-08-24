n = int(input())


result = ''
count=1
for i in range(n):
    for j in range(n):
        result += '{} '.format(count+n*j)
    count += 1
    result += '\n'
print(result)
