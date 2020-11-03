import sys
sys.stdin = open("input_data/3분할1.txt")

T = int(input())
T = 1
for test_case in range(1, T+1):
    N = int(input())
    arrs = list(map(int, input().split()))


    def divide_3(k, sums):
        if k == 3:
            print(sums)
            return
        else:
            for i in range(k, N-1):
                divide_3(k+1, sums + arrs[i])

    divide_3(0, 0)