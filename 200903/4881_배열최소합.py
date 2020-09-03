import sys

sys.stdin = open("input_data/4881.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    visit = [0] * N


    A = [0] * N
    mins = 10000
    def dfs(k, N, result):
        global mins
        if result > mins:
            return
        if k == N :
            if mins >= result:
                mins = result
            return
        else:
            for i in range(N):
                if visit[i] == 0:
                    visit[i] = 1
                    dfs(k+1, N, result + arr[k][i])
                    for i
                    visit[i] = 0

    dfs(0, N, 0)
    print('#{} {}'.format(test_case, mins))