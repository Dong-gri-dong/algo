import sys
sys.stdin = open("input_data/4012.txt")

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


def subset(k):
    if k == N:
        if len(A) == len(B):
            diff = 0
            for i in A:
                for j in A:
                    diff += arr[i][j]
            for i in B:
                for j in B:
                    diff -= arr[i][j]
            global ans; ans = min(ans, abs(diff))

    else:
        A.append(k)
        subset(k+1)
        A.pop()

        B.append(k)
        subset(k + 1)
        B.pop()

    A = []
    B = []
    subset(0)
    print(ans)