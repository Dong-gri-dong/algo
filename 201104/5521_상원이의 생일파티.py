import sys
sys.stdin = open("input_data/5521_상원이의 생일파티.txt")


def bfs(v):
    Q = []
    Q.append(v)
    visit[v] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if visit[w] != 0:
                continue
            Q.append(w)
            visit[w] = visit[v] + 1

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(M)]
    visit = [0] * (N + 1)
    G = [[] for _ in range(N+1)]

    for i in range(M):
        s, e = temp[i]
        G[s].append(e)
        G[e].append(s)

    bfs(1)
    result = 0
    for i in visit:
        if 1 < i <=3:
            result += 1

    print('#{} {}'.format(test_case, result))

