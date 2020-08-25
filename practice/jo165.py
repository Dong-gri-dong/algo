
n = 5
lists = [[0]*n for i in range(5)]



for i in range(n):
    for k in range(n):
        lists[i][k] = 0

one_list = [0,2,4]

for i in one_list:
    lists[0][i] = 1

for i in range(1, n):
    for k in range(0, n):
        if k-1 >= 0:
            lists[i][k] += lists[i-1][k-1]
        if k+1 < n:
            lists[i][k] += lists[i - 1][k + 1]

result =''
for i in range(0, n):
    for k in range(0, n):
        result += '{} '.format(lists[i][k])
    result += '\n'
print(result)