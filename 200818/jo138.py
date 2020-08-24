n = int(input())


result=''
for i in range(1, n+1):
    for n in range(1, n+1):
        result += '{} '.format(str((i,n)))
    result += '\n'
print(result)