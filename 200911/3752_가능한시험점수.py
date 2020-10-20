import sys

sys.stdin = open("input_data/3752.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    visit = [[0] * (sum(score) +1) for _ in range(N+1)]# 마지막에 중복을 제거

    # def dfs(k, s):
    #     if visit[k][s]:
    #         return
    #     visit[k][s] = 1
    #     if k == N:
    #         return
    #     else:
    #         dfs(k+1, s)
    #         dfs(k+1, s + score[k])
    # dfs(0, 0)

    visit = [0] * (sum(score) + 1)
    Q = [[0, 0]]
    while Q:
        k, s = Q.pop(0)
        if k ==N:
            visit[s] = 1
        else:
            Q.append([k + 1, s])
            Q.append([k + 1, s+score[k]])




    print('#{} {}'.format(test_case, sum(visit)))







