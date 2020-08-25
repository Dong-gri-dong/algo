n, number = list(map(int, input().split()))
result = ''

if number == 1:
    count = 1
    for i in range(n):
        for j in range(n):
            result += '{} '.format(count)
        count += 1
        result += '\n'

elif number == 2:
    count = 0
    for i in range(n):

        if i % 2:
            for j in range(n):
                result += '{} '.format(count)
                count -= 1
        else:
            for j in range(n):
                result += '{} '.format(count+1)
                count += 1
        result += '\n'

elif number == 3:
    count = 1
    for i in range(n):
        for j in range(n):
            result += '{} '.format(count*(j+1))
        count += 1
        result += '\n'


print(result)
