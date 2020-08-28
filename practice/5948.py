import sys
import pprint
sys.stdin = open('input_data/5948.txt')

T = int(input())

for test_case in range(1, T+1):


    arr = list(map(int, input().split()))

    n = len(arr)
    total = 1 << n

    part = []





    for i in range(total):
        count = 0
        sums = 0
        for j in range(n):
            if i&(1<<j):
                sums += arr[j]
                count += 1
        if count == 3:
            part.append(sums)


    print('#{} {}'.format(test_case, sorted(list(set(part)), reverse= True)[4]))


