n = int(input())

number=[1, 3, 5, 7, 9]

result=''
k = 0
j = 1
for i in range(1, n+1):
    for u in range(1, n+1):

        if k == 5:
            k = 0
        result += '{} '.format(str(number[k]))
        k += 1
        if j % n == 0:
            result += '\n'
        j+=1
print(result)