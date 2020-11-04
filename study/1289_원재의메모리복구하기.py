import sys
sys.stdin = open("input_data/1289_원재의메모리복구하기.txt")

T = int(input())



def memory(i, n):
    while i < N:
        start[i] = n
        i += 1

for test_case in range(1, T+1):
    arr = list(map(int, input()))
    N = len(arr)
    start = [0]*len(arr)
    result = 0
    while arr != start:
        for i in range(len(arr)):
            if arr[i] != start[i]:

                n = arr[i]
                break
        memory(i, n)
        result += 1



    print('#{} {}'.format(test_case, result))
