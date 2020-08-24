n = list(map(int, input().split()))

result = [0]*6
for i in n:
    result[i-1] += 1

for idx, i in enumerate(result):
    print('{} : {}'.format(idx+1, i ))