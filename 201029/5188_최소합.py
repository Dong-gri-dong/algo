import sys
sys.stdin = open("input_data/5188_최소합.txt")

T = int(input())

dx = [0, 1]
dy = [1, 0]

for test_case in range(1, T+1):
    N = int(input())

    arrs = [list(map(int, input().split())) for _ in range(N)]


    def dfs(y, x, sums):
        global result
        if sums >= result:
            return
        if y == N-1 and x == N-1:
            if sums <= result:
                result = sums
            return
        else:
            for i in range(2):
                tx = dx[i] + x
                ty = dy[i] + y
                if tx == N or ty == N:
                    continue
                dfs(ty, tx, sums + arrs[ty][tx])

    result = 100000000000000
    dfs(0, 0, arrs[0][0])
    print('#{} {}'.format(test_case, result))