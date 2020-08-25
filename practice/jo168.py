n = int(input())


result = [1]
final = ''
c =[]
for i in range(0, n):
    a = result[:]

    for k in range(i):
        result[1+k] = a[k]+result[1+k]
    final =''
    for u in range(len(result)):
        final += '{} '.format(result[u])
    c.append(final)
    result.append(0)


result = ''
for i in range(1,n+1):
    result += '{}\n'.format(c[-i])
print(result)