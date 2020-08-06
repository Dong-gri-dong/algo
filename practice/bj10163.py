import sys

sys.stdin = open('input_data/bj_10163.txt')

T = int(input())
arr = [[0 for i in range(101)] for k in range(101)]

for t in range(1, T+1):
    num = list(map(int, input().split()))

    for i in range(num[0] , num[0]+num[2]):
        for n in range(num[1], num[1]+num[3]):
            arr[i][n] = t

for k in range(1, T+1):
    arr_count = 0
    for i in range(len(arr)):
        arr_count += arr[i].count(k)
    print(arr_count)
