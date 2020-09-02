import sys

sys.stdin = open("input_data/bj_15649")

T = int(input())

for test_case in range(1, T+1):
    n, c = map(int, (input().split()))


    arr = list(range(1,n+1))
    A = [0] * n

    def nm(k, n, c):
        if k == c:
            for j in range(c):
                print(arr[j], end = " ")
            print()


        else:
            for i in range(k, n):
                arr[k], arr[i] = arr[i], arr[k]
                nm(k+1, n, c)
                arr[k], arr[i] = arr[i], arr[k]

    nm(0, n, c)