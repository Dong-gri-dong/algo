import sys

sys.stdin = open('input_data/4837.txt')


T = int(input())
arr = [i for i in range(1, 13)]

for t in range(1, T + 1):
    spec = list(map(int, input().split()))
    count = 0
    for i in range(1<<len(arr)):
        result = []
        for j in range(len(arr)):

            if i &(1<<j):
                #print(i, 1<<j)
                #print(i &(1<<j))
                #print()
                result.append(arr[j])
                #print(arr[j], end=' ')
        if sum(result) == spec[1] and len(result) == spec[0]:
            count += 1





    print('#{} {}'.format(t, count))


