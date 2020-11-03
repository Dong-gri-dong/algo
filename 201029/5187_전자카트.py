import sys
sys.stdin = open("input_data/5189_전자카트.txt")


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arrs = [list(map(int, input().split())) for _ in range(N)]

    visit = [0]*(N+1)
    visit[1] = 1
    def bfs(k, n, sums, pre):
        global result
        if k == n-1:
            if result >= sums+arrs[pre][0]:
                result = sums+arrs[pre][0]
            return
        else:
            for i in range(0, N):
                if visit[i+1] == 1:
                    continue
                visit[i+1] = 1
                bfs(k+1, n, sums + arrs[pre][i], i)
                visit[i+1] = 0
    result = 10000000000000000
    bfs(0, N, 0, 0)
    print('#{} {}'.format(test_case, result))